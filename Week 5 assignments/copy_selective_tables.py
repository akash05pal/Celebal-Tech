import sqlite3
import pandas as pd

def copy_selective_tables(src_db, dest_db, table_columns):
    src_conn = sqlite3.connect(src_db)
    dest_conn = sqlite3.connect(dest_db)
    for table, columns in table_columns.items():
        cols = ', '.join(columns)
        df = pd.read_sql_query(f'SELECT {cols} FROM {table}', src_conn)
        df.to_sql(table, dest_conn, if_exists='replace', index=False)
    src_conn.close()
    dest_conn.close()

# Example usage:
# table_columns = {'table1': ['col1', 'col2'], 'table2': ['col3']}
# copy_selective_tables('source.db', 'destination.db', table_columns) 