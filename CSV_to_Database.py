import pandas as pd
import mysql.connector
from mysql.connector import errorcode
import os

# Path to folder containing csv files
folder_path='D:\\Projects\\Dataset\\Target_Ecommerce\\archive'

#List of csv files and their corresponding table names.
csv_files = [
    ('customers.csv','customers'),
    ('geolocation.csv','geolocation'),
    ('order_items.csv','order_items'),
    ('orders.csv','orders'),
    ('payments.csv','payments'),
    ('products.csv','products'),
    ('sellers.csv','sellers')    
]
try:
    conn = mysql.connector.connect(
        host = '####',
        user = '####',
        password = '#######'
    )
    print("Database Connection Successful!")
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS target_ecommerce")

    # function to return sql datatype from pandas
    def get_sql_type(dtype):
        if pd.api.types.is_integer_dtype(dtype):
            return 'INT'
        elif pd.api.types.is_float_dtype(dtype):
            return 'FLOAT'
        elif pd.api.types.is_bool_dtype(dtype):
            return 'BOOLEAN'
        elif pd.api.types.is_datetime64_any_dtype(dtype):
            return 'DATETIME'
        else:
            return 'TEXT'

    for csv_file,table_name in csv_files:
        file_path = os.path.join(folder_path,csv_file) 
        
        df = pd.read_csv(file_path) # Read csv file as pandas dataframe
        df = df.where(pd.notnull(df),None) # Replace NaN with None to handle sql NULL
        
        # Debugging: Check for NaN values
        print(f"Processing {csv_file}")
        print(f"NaN values before replacement:\n{df.isnull().sum()}\n")
        
        # Clean column names
        df.columns = [col.replace(' ',"_").replace('-','_').replace('.','_') for col in df.columns]
        
        # CREATE TABLE statement with appropriate data types
        columns = ', '.join([f'`{col}` {get_sql_type(df[col].dtype)}' for col in df.columns])
        cursor.execute("USE target_ecommerce")
        create_table_query = f'CREATE TABLE IF NOT EXISTS `{table_name}` ({columns})'
        cursor.execute(create_table_query)
        
        # Insert Dataframe data into sql table
        for _, row in df.iterrows():
            # Converting row to tuple and handle NaN/None explicitly
            values = tuple(None if pd.isna(x) else x for x in row)
            sql = f"INSERT INTO `{table_name}` ({', '.join(['`' + col + '`' for col in df.columns])}) VALUES ({', '.join(['%s'] * len(row))})"
            cursor.execute(sql, values)
        
        # Commit transaction for the current csv file
        conn.commit()
        
        
        
    conn.close()
    print("Database Closed!")
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    else: print(err)
except Exception as err:
    print(err)