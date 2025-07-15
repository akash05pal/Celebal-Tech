import sqlite3
import pandas as pd
from fastavro import writer, parse_schema

def export_table_to_avro(db_path, table_name, avro_path):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(f'SELECT * FROM {table_name}', conn)
    records = df.to_dict(orient='records')
    schema = {
        'doc': f'Avro schema for {table_name}',
        'name': table_name,
        'namespace': 'example.avro',
        'type': 'record',
        'fields': [
            {'name': col, 'type': ['null', 'string']} for col in df.columns
        ]
    }
    with open(avro_path, 'wb') as out:
        writer(out, parse_schema(schema), records)
    conn.close()

# Example usage:
# export_table_to_avro('source.db', 'my_table', 'output.avro') 