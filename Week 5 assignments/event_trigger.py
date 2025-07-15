import time
import os

def watch_file(path, callback):
    seen = set(os.listdir(path))
    while True:
        current = set(os.listdir(path))
        new_files = current - seen
        if new_files:
            for f in new_files:
                callback(f)
        seen = current
        time.sleep(5)

def on_new_file(filename):
    print(f'New file detected: {filename}')

# Example usage:
# watch_file('/path/to/watch', on_new_file) 