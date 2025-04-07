# Step 1:  Load CSV Files into SQLLite (DONE
# Step 2:  Create Tables Dynamically from CSV (DONE)
# Step 3:  Handle Schema Conflicts (DONE)
    # For example if two tables have the same column names but different data types
    # I think for our purposes we'll treat conflicts with the following approach:
    # If the new data follows the same structure as the current data, we'll just add the new data
    # If the new data has a different structure, we'll replace the old data with the most recent data
# Step 4:  Simulate AI using input (the input to be schemas)
# Step 5:  Add AI to generate SQL Queries

import sqlite3
from query_generator import QueryGenerator
import csv
import os
import pandas as pd

class SheetsAI:
    def __init__(self, db_name='SheetsAI.db', api_key=None):
        '''Constructor to initialize the database connection and AI query generator'''
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.query_generator = QueryGenerator(api_key) if api_key else None

    def table_exists(self, table_name):
        '''Function that checks if a table exists in the database'''
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        return bool(self.cursor.fetchone())
    
    def get_table_schema(self, table_name):
        '''Function that gets the schema of a table'''
        self.cursor.execute(f"PRAGMA table_info({table_name})")
        schema = {row[1]: row[2] for row in self.cursor.fetchall()}
        return schema
    
    def get_csv_schema(self, df):
        '''Function that gets the schema of a csv file'''
        return {col: 'TEXT' for col in df.columns}
    
    def add_csv_to_database(self, csv_file):
        '''Function that adds a csv file to the database while checking for schema conflicts'''
        df = pd.read_csv(csv_file)
        table_name = os.path.splitext(os.path.basename(csv_file))[0]
        if self.table_exists(table_name):
            # If the table exists, check for schema conflicts
            existing_schema = self.get_table_schema(table_name)
            new_schema = self.get_csv_schema(df)
            
            # Check for schema conflicts
            if existing_schema != new_schema:
                print(f"Schema conflict in table: {table_name}. Replacing old data.")
                df.to_sql(table_name, self.connection, if_exists='replace', index=False)
            else:
                print(f"Schema is the same for table: {table_name}. Adding new data.")
                df.to_sql(table_name, self.connection, if_exists='append', index=False)
        else:
            # If the table does not exist, create it
            print(f"Table does not exist yet, creating new table: {table_name}.")
            df.to_sql(table_name, self.connection, if_exists='replace', index=False)

    def execute_sql_query(self, query):
        '''Function that executes an SQL query'''
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            return f"SQL Error: {e}"
    
    def ask_database(self, user_prompt, table_name):
        '''Function that takes a user prompt and generates an SQL query'''
        if not self.query_generator:
            return "AI query generator has not been intialized. Please provide a valid key."
        
        sql_query = self.query_generator.generate_sql_query(user_prompt, table_name)
        print(f"Generated SQL Query: {sql_query}")
        return self.execute_sql_query(sql_query)

    def close_connection(self):
        '''Function that closes the connection to the database'''
        self.connection.close()

    def __del__(self):
        '''Destructor to ensure the connection is closed'''
        self.close_connection()

