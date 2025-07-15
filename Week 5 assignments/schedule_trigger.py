import schedule
import time

def job():
    print('Pipeline executed!')

schedule.every().day.at('01:00').do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

# Adjust the schedule as needed for your use case. 