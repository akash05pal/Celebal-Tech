import sqlite3
import pandas as pd

def export_table_to_csv(db_path, table_name, csv_path):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(f'SELECT * FROM {table_name}', conn)
    df.to_csv(csv_path, index=False)
    conn.close()

# Example usage:
# export_table_to_csv('source.db', 'my_table', 'output.csv') 