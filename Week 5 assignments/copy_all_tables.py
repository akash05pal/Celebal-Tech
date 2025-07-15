import sqlite3
import pandas as pd

def copy_all_tables(src_db, dest_db):
    src_conn = sqlite3.connect(src_db)
    dest_conn = sqlite3.connect(dest_db)
    src_cursor = src_conn.cursor()
    dest_cursor = dest_conn.cursor()
    src_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in src_cursor.fetchall()]
    for table in tables:
        df = pd.read_sql_query(f'SELECT * FROM {table}', src_conn)
        df.to_sql(table, dest_conn, if_exists='replace', index=False)
    src_conn.close()
    dest_conn.close()

# Example usage:
# copy_all_tables('source.db', 'destination.db') 