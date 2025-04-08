# This file will serves as the main script the user will utilize.
# Users will be able to import their CSV files and create tables via sqlite3.
# Users can then query the tables via SQL queries.

from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

import SheetsAI as SheetsAI
import os
import pandas as pd
import sqlite3

def get_api_key():
    """Function to get the OpenAI API key from the user."""
    return os.getenv("OPENAI_API_KEY")

def main():
    print("Welcome to SheetsAI!")
    print("This program allows you to import CSV files and create tables in a SQLite database.")
    print("You can then query the tables using natural language.")

    api_key = get_api_key()

    # Initialize the SheetsAI class
    sheets_ai = SheetsAI.SheetsAI(api_key=api_key)

    # Loop to allow the user to import multiple CSV files
    while True:
        csv_file = input("Enter the path to the CSV file (or 'done' to finish uploading): ")
        if csv_file.lower() == 'done':
            break
        if not os.path.exists(csv_file):
            print("File does not exist. Please try again.")
            continue
        else:
            sheets_ai.add_csv_to_database(csv_file)
            print(f"CSV file '{csv_file}' has been imported successfully.")
        print("Your CSV file has succesfully been imported into the database.")
    
    print("\nYou can now query the tables using natural language.")
    print("Type 'list tables' to see all available tables or 'exit' to quit.")
    # Loop to allow the user to query the database
    while True:
        user_prompt = input("Enter your query (or type 'exit'): ").strip().lower()
        if user_prompt == 'exit':
            break
        if user_prompt == 'list tables':
            tables = sheets_ai.list_tables()
            print("Available tables:", ", ".join(tables) if tables else "No tables found.")
        
        table_name = input("Enter the table name you want to query: ").strip()

        try:
            result = sheets_ai.ask_database(user_prompt, table_name)
            print("Query Result:")
            if isinstance(result, str):
                print(result)
            else:
                for row in result:
                    print(row)
        except Exception as e:
            print(f"An error occurred: {e}")

    # Close the database connection
    print("Exiting the program. Goodbye!")
    sheets_ai.close_connection()

if __name__ == "__main__":
    main()