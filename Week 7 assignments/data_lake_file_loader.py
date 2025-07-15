import os
import re
import pandas as pd
import sqlite3  # Replace with your DB connector (e.g., pyodbc for Azure SQL)
from datetime import datetime

def extract_date_from_filename(filename, pattern, date_format):
    match = re.search(pattern, filename)
    if match:
        date_str = match.group(1)
        return datetime.strptime(date_str, date_format)
    return None

def process_cust_mstr(file_path, conn):
    filename = os.path.basename(file_path)
    date_obj = extract_date_from_filename(filename, r'CUST_MSTR_(\d{8})', '%Y%m%d')
    if date_obj is None:
        raise ValueError(f"Date not found in filename: {filename}")
    df = pd.read_csv(file_path)
    df['date'] = date_obj.strftime('%Y-%m-%d')
    conn.execute('DELETE FROM CUST_MSTR')
    df.to_sql('CUST_MSTR', conn, if_exists='append', index=False)

def process_master_child(file_path, conn):
    filename = os.path.basename(file_path)
    date_obj = extract_date_from_filename(filename, r'master_child_export-(\d{8})', '%Y%m%d')
    if date_obj is None:
        raise ValueError(f"Date not found in filename: {filename}")
    df = pd.read_csv(file_path)
    df['date'] = date_obj.strftime('%Y-%m-%d')
    df['date_key'] = date_obj.strftime('%Y%m%d')
    conn.execute('DELETE FROM master_child')
    df.to_sql('master_child', conn, if_exists='append', index=False)

def process_h_ecom_order(file_path, conn):
    df = pd.read_csv(file_path)
    conn.execute('DELETE FROM H_ECOM_Orders')
    df.to_sql('H_ECOM_Orders', conn, if_exists='append', index=False)

def main(data_lake_dir, db_path):
    conn = sqlite3.connect(db_path)
    for fname in os.listdir(data_lake_dir):
        fpath = os.path.join(data_lake_dir, fname)
        if fname.startswith('CUST_MSTR_') and fname.endswith('.csv'):
            process_cust_mstr(fpath, conn)
        elif fname.startswith('master_child_export-') and fname.endswith('.csv'):
            process_master_child(fpath, conn)
        elif fname.startswith('H_ECOM_ORDER') and fname.endswith('.csv'):
            process_h_ecom_order(fpath, conn)
    conn.close()

# Example usage:
# main('/path/to/data_lake', 'mydatabase.db') 