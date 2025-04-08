import unittest
import os
import sqlite3
import pandas as pd
from src.SheetsAI import SheetsAI

class TestSheetsAI(unittest.TestCase):
    def setUp(self):
        self.db_name = 'TestSheetsAI.db'
        self.sheets_ai = SheetsAI(db_name=self.db_name)

        # Create a sample dataframe
        self.sample_csv_path = 'test_users.csv'
        df = pd.DataFrame({
            'name': ['Alice', 'Bob'],
            'age': [30, 45],
            'salary': [100000, 85000]
        })
        df.to_csv(self.sample_csv_path, index=False)

    def tearDown(self):
        self.sheets_ai.close_connection()
        if os.path.exists(self.db_name):
            os.remove(self.db_name)
        if os.path.exists(self.sample_csv_path):
            os.remove(self.sample_csv_path)

    def test_add_csv_to_database(self):
        self.sheets_ai.add_csv_to_database(self.sample_csv_path)
        tables = self.sheets_ai.list_tables()
        self.assertIn('test_users', tables)

    def test_table_schema(self):
        self.sheets_ai.add_csv_to_database(self.sample_csv_path)
        schema = self.sheets_ai.get_table_schema('test_users')
        self.assertEqual(schema, {'name': 'TEXT', 'age': 'TEXT', 'salary': 'TEXT'})

    def test_query_execution(self):
        self.sheets_ai.add_csv_to_database(self.sample_csv_path)
        result = self.sheets_ai.execute_sql_query("SELECT name FROM test_users WHERE salary > 90000")
        self.assertEqual(result, [('Alice',)])

if __name__ == '__main__':
    unittest.main()
