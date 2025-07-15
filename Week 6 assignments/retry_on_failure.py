import time

def retrieve_data_with_retry(retrieve_func, max_retries=3, wait_seconds=5):
    for attempt in range(max_retries):
        try:
            return retrieve_func()
        except Exception as e:
            print(f"Attempt {attempt+1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(wait_seconds)
            else:
                raise

# Example usage:
# def get_data():
#     # Your data retrieval logic here
#     pass
# retrieve_data_with_retry(get_data) 