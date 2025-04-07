# This file will serves as the main script the user will utilize.
# Users will be able to import their CSV files and create tables via sqlite3.
# Users can then query the tables via SQL queries.

import SheetsAI
import os
import pandas as pd
import sqlite3

def main():
    print("Welcome to SheetsAI!")
    print("This program allows you to import CSV files and create tables in a SQLite database.")
    print("You can then query the tables using SQL queries.")

    # Initialize the SheetsAI class
    sheets_ai = SheetsAI.SheetsAI()
    # Create the database if it doesn't exist
    if not os.path.exists(sheets_ai.db_name):
        sheets_ai.connection = sqlite3.connect(sheets_ai.db_name)
        sheets_ai.cursor = sheets_ai.connection.cursor()

    # Loop to allow the user to import multiple CSV files
    print("A database has been intialized for you, feel free to import CSV files.")
    print("To query the database, you can use utilize SheetsAI unqiue feature of simply passing natural questions.")
    print("For example, try passing the prmopt 'List all the tables in the database'.")
    while True:
        csv_file = input("Enter the path to the CSV file (or 'exit' to quit): ")
        if csv_file.lower() == 'exit':
            break
        if not os.path.exists(csv_file):
            print("File does not exist. Please try again.")
            continue
        sheets_ai.add_csv_to_database(csv_file)
        print(f"CSV file '{csv_file}' has been imported successfully.")
