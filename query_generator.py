import openai
# Note to users: This code was written by OpenAI's GPT-4 model.

class QueryGenerator:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_sql_query(self, user_prompt, table_name):
        """Use OpenAI to convert natural language into an SQL query."""
        prompt = f"""
        You are an AI assistant that converts natural language questions into SQL queries.
        The user is working with an SQLite database. The table name is {table_name}.
        
        Example Inputs:
        - "Show me all the rows."
        - "Get the total sales from March."
        - "Find all customers from New York."

        Example Output:
        - "SELECT * FROM {table_name};"
        - "SELECT SUM(sales) FROM {table_name} WHERE month='March';"
        - "SELECT * FROM {table_name} WHERE city='New York';"

        User Input: {user_prompt}
        SQL Query:
        """

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": prompt}],
            temperature=0  # Ensures more consistent queries
        )

        return response["choices"][0]["message"]["content"].strip()
