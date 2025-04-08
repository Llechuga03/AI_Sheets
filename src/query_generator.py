import openai
# Note to users: This code was written by OpenAI's GPT-4 model.

class QueryGenerator:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_sql_query(self, user_prompt, table_name, schema=None):
        """Use OpenAI to convert natural language into an SQL query."""
        column_info = ", ".join([f"{col} ({dtype})" for col, dtype in schema.items()]) if schema else "unknown columns"
    
        prompt = f"""
        You are an AI assistant that converts natural language questions into SQL queries.
        The user is working with an SQLite database. The table name is '{table_name}'.
        The table contains the following columns: {column_info}.

        Convert the following user request into an SQL query.
    
        User Input: {user_prompt}
        SQL Query:
        """

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": prompt}],
            temperature=0
        )

        return response["choices"][0]["message"]["content"].strip()

