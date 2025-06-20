# AI_Sheets Project

## Author
<p>I'm Logan Lechuga, and I created this program as a school project which transformed into a personal project I wanted to improve and iterate on. The project demonstrates proper use of unit testing, utilizing API's, database management, modular software design, and continuous integration. Although the code is mostly complete as of this latest commit, there is still room for improvement. In future updates, I hope to use docker in order to make it easier for others to use the program, and maybe create a GUI for the application. One important fact to keep in mind is that this tool requires an OpenAI API key in order to use it, and I don't want to give that out for anyone to use. With that said, I have provided a video below that showcases a demo of the application. Note that some of the files in this repository were created with the assistance of Chat-GPT, such as the query_generator.py file. Hope you enjoy the project!</p>

## Querying CSV Files with Natural Language -- A Brief Overview
<p>The goal of this project is to create an equivalent to Excel or Google Sheet application with the additional feature of having an AI assistant parse through the files based on your requests.  Utilizing a SQLite database we can store CSV files in their own tables and then query through the tables use OpenAI's GPT-4o model through backend APIs. The user can query through the CSV files once they are uploaded using natural prompts like "Show me all professors in the engineering department." which will then be turned into an equivalent SQL command and executed.</p>

## 🌟 Highlights
The project follows the following five steps to achieve it's goals while utilizing a basic CLI. 

    Step 1:  Load CSV Files into SQLLite
    Step 2:  Create Tables Dynamically from imported CSV Files
    Step 3:  Handle Schema Conflicts 
    Step 4:  Simulate AI using input (the input to be schemas)
    Step 5:  Utilizie GPT-4o model to generate SQL Queries and then execute them

## Have your own OpenAI API Key?
<p>For users that have their own OpenAI API key, you can enter this key in the .yourenv text file and use the application as shown in the demo video.</p>

## Usage Instructions
In order to use the program, follow the instructions below. Note, the program may take up to 10 seconds to run upon intial call.

 1. Clone this repository via copying the URL or downloading the zip file.
 2. Install the necessary requirements once you have cloned and opened the repo,
    
     ``` bash
     pip install -r requirements.txt
     ```

3. Run the main program and follow the instructions displayed on your terminal.
   
   ``` bash
   python user_program.py
   ```
    
