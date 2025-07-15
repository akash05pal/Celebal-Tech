from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum, count, avg, row_number, desc, window, max as _max
from pyspark.sql.window import Window

# Initialize Spark session
spark = SparkSession.builder.appName("NYC Taxi Analysis").getOrCreate()

# Load CSV data from DBFS or local path
# df = spark.read.csv("/mnt/data/yellow_tripdata_2020-01.csv", header=True, inferSchema=True)
df = spark.read.csv("yellow_tripdata_2020-01.csv", header=True, inferSchema=True)

df.createOrReplaceTempView("taxi")

# Query 1: Add 'Revenue' column
revenue_cols = ['fare_amount','extra','mta_tax','improvement_surcharge','tip_amount','tolls_amount','total_amount']
df = df.withColumn('Revenue', sum([col(c) for c in revenue_cols]))

# Query 2: Passenger count by area (assuming 'PULocationID' as area)
passenger_by_area = df.groupBy('PULocationID').agg(_sum('passenger_count').alias('total_passengers'))

# Query 3: Realtime average fare/total earning by vendor
avg_fare_by_vendor = df.groupBy('VendorID').agg(avg('fare_amount').alias('avg_fare'), avg('total_amount').alias('avg_total_earning'))

# Query 4: Moving count of payments by payment mode (using window of 10 minutes as example)
payment_count_window = df.withColumn('pickup_datetime', col('tpep_pickup_datetime').cast('timestamp')) \
    .groupBy(window('pickup_datetime', '10 minutes'), 'payment_type') \
    .agg(count('*').alias('payment_count'))

# Query 5: Top 2 vendors by revenue on a date, with passenger and distance
from pyspark.sql.functions import to_date

df_with_date = df.withColumn('date', to_date('tpep_pickup_datetime'))
vendor_stats = df_with_date.groupBy('date', 'VendorID').agg(
    _sum('total_amount').alias('total_revenue'),
    _sum('passenger_count').alias('total_passengers'),
    _sum('trip_distance').alias('total_distance')
)
window_spec = Window.partitionBy('date').orderBy(desc('total_revenue'))
top2_vendors = vendor_stats.withColumn('rank', row_number().over(window_spec)).filter(col('rank') <= 2)

# Query 6: Most passengers between two locations
route_passengers = df.groupBy('PULocationID', 'DOLocationID').agg(_sum('passenger_count').alias('total_passengers'))
most_passenger_route = route_passengers.orderBy(desc('total_passengers')).limit(1)

# Query 7: Top pickup locations with most passengers in last 5/10 seconds (assuming streaming context)
# This is a placeholder; in real streaming, use structured streaming and watermarking
# For batch, get top pickup locations in last 10 seconds of data
from pyspark.sql.functions import unix_timestamp
max_time = df.agg(_max(unix_timestamp('tpep_pickup_datetime'))).collect()[0][0]
top_pickups_10s = df.withColumn('pickup_unix', unix_timestamp('tpep_pickup_datetime')) \
    .filter(col('pickup_unix') >= max_time - 10) \
    .groupBy('PULocationID').agg(_sum('passenger_count').alias('total_passengers')) \
    .orderBy(desc('total_passengers'))

# Save results as needed, e.g.,
# passenger_by_area.write.csv('passenger_by_area.csv')
# avg_fare_by_vendor.write.csv('avg_fare_by_vendor.csv')

# Stop Spark session
spark.stop() 