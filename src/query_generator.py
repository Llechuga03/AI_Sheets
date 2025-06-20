import openai
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
# Note to users: This code was written by OpenAI's GPT-4 model.

class QueryGenerator:
    def __init__(self, api_key=None):
        '''Constructor to initialize the OpenAI API key'''
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.api_key = openai.api_key

    def generate_sql_query(self, user_prompt, table_name, schema): #got rid of schema equal to None, might have to change this back
        from openai import OpenAI
        client = OpenAI(api_key=self.api_key)

        messages = [
            {
                "role": "system",
                "content": (
                    "You are an AI assistant that converts natural language questions into SQL queries. "
                    "The user is working with an SQLite database."
                ),
            },
            {
                "role": "user",
                "content": f"The table name is '{table_name}' and its schema is: {schema}. "
                f"Now generate an SQL query for: {user_prompt}",
            },
        ]

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0,
        )

        raw_query = response.choices[0].message.content.strip()

        # Remove code block markers if they exist
        if raw_query.startswith("```"):
            raw_query = "\n".join(line for line in raw_query.splitlines() if not line.strip().startswith("```"))

        return raw_query


