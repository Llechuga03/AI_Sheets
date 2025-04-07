# AI_Sheets
The goal of this project is to create an equivalent to Excel or Google Sheet application where the interaction with the application is a chat interaction using openAI. The project follows the following five steps to achieve it's goals. 
Step 1:  Load CSV Files into SQLLite (DONE)
Step 2:  Create Tables Dynamically from CSV (DONE)
Step 3:  Handle Schema Conflicts (DONE)
    I think for our purposes we'll treat conflicts with the following approach:
    If the new data follows the same structure as the current data, we'll just add the new data.
    If the new data has a different structure, we'll replace the old data with the most recent data
Step 4:  Simulate AI using input (the input to be schemas)
Step 5:  Add AI to generate SQL Queries
