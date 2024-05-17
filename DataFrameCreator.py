from SQLSTUFF.ConnectToDatabase import ConnectToDatabase  # Import the ConnectToDatabase class
import mysql.connector
import pandas as pd
 
class DataFrameCreator:
   
    @staticmethod
    # For columns arg, write them as a single string using SQL syntax required for a SELECT query
    def dataframe_creator(columns: str, table: str, database_name='northwind'):
        try:
            database = ConnectToDatabase.connect_to_database(database_name)  # Instantiate the ConnectToDatabase class
            query = "SELECT " + columns + " FROM " + table
            df = pd.read_sql(query, database)
            database.close()
            return df
        except mysql.connector.Error as e_sql:
            print(f"MySQL Error creating dataframe: {e_sql}")
            return None
