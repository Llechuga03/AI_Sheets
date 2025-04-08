# AI_Sheets Project

## Author
<p>I'm Logan Lechuga, and I created this program as a school project. The project demonstrates proper use of unit testing, utilizing API's, database management, modular software design, and Continuous Inegration. Although the code is mostly complete as of this latest commit, there is still room for improvement. Note that some of the files in this repository were created with the assistance of Chat-GPT, such as the query_generator.py file. Hope you enjoy the project!</p>

## Querying CSV Files with Natural Language -- A Brief Overview
<p>The goal of this project is to create an equivalent to Excel or Google Sheet application where the interaction with the application is a chat interaction using openAI. Utilizing a SQLite database we can store CSV files in their own tables and then query through the tables use OpenAI's GPT-4o model through backend APIs. The user can query through the CSV files once they are uploaded using natural prompts like "Show me all professors in the engineering department."</p>

## 🌟 Highlights
The project follows the following five steps to achieve it's goals while utilizing a basic CLI. 

    - Step 1:  Load CSV Files into SQLLite
    - Step 2:  Create Tables Dynamically from CSV 
    - Step 3:  Handle Schema Conflicts 
    - Step 4:  Simulate AI using input (the input to be schemas)
    - Step 5:  Utilizie GPT-4o model to generate SQL Queries and then execute them

## Usage Instructions
In order to use the program, follow the instructions below. Note, the program may take up to 15 seconds to run upon intial call.

    1. Clone this repository via copying the URL or downloading the zip file.
    2. Install the necessary requirements once you have cloned and opened the repo,
    ``` bash
    pip install -r requirements.txt
    ```
    3. Run the main program and follow the instructions displayed on your terminal.
    ``` bash
    python user_program.py
    ```
    
