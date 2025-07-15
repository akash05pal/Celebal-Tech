import sqlite3
import pandas as pd

def export_table_to_parquet(db_path, table_name, parquet_path):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(f'SELECT * FROM {table_name}', conn)
    df.to_parquet(parquet_path, index=False)
    conn.close()

# Example usage:
# export_table_to_parquet('source.db', 'my_table', 'output.parquet') 