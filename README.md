# AI_Sheets Project

## Author
<p>I'm Logan Lechuga, and I created this program as a school project which transformed into a personal project I wanted to improve and iterate on. The project demonstrates proper use of unit testing, using GitHub actions for CI/CD, utilizing API's, database management, and modular software design. Although the code is mostly complete as of this latest commit, there is still room for improvement. In future updates, I hope to use docker in order to make it easier for others to use the program, and maybe create a GUI for the application. One important fact to keep in mind is that this tool requires an OpenAI API key in order to use it, and I don't want to give that out for anyone to use. With that said, I have provided a video below that showcases a demo of the application. Note that some of the files in this repository were created with the assistance of Chat-GPT, such as the query_generator.py file. Hope you enjoy the project!</p>

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
<p>For users that have their own OpenAI API key, you can enter this key in the .env file and use the application as shown in the demo video.</p>

## Video Demo
<p>Following this link will take you to a video demo of the application. This is mainly for users who don't have an OpenAI key or for those who just want a "relatively" quick demonstration of how the application works. <a href="https://youtu.be/9PxT78pqYMk" alt="Demo of application">Click here for Demo</a></p>

## Usage Instructions -> Cloning the Repo
In order to use the program, follow the instructions below. Note, the program may take up to 10 seconds to run upon intial call.

 1. Clone this repository via copying the URL or downloading the zip file.
 2. Install the necessary requirements once you have cloned and opened the repo,
    
     ``` bash
     pip install -r requirements.txt
     ```

3. If you have your own OpenAI API key, create an .env file and create a variable called OPENAI_API_KEY and assign it the key value.
4. Add the CSV files you want to query through to the data folder. Note you can delete the CSV files that already exist as those are simply for testing purposes.

5. Run the main program and follow the instructions displayed on your terminal.
   
   ``` bash
   python user_program.py
   ```
    
## Usage Instructions -> Docker
If you want to skip cloning the repository you can simply login to docker from your terminal and then follow the steps below.
 1. After logging in, navigate to the directory where your csv files are stored.
 2. Next, run the following command which starts up a container with a unique name in the background.
``` bash
     docker run -dit --name yourcontainername yourusername/sheetsai
```
 3. Next, use the following command to copy over your files into the data folder inside the docker container.
``` bash
     docker cp filename.csv yourcontainername:/app/data
``` 
 4. You can now attach to the container using the following command. Note that the introductory message will not appear since we started the container in the background. After running the command below you will see an empty line, I recommend pressing 5 to get the help message to pop up.
``` bash
     docker attach yourcontainername
``` 
 5. Once inside the container you can begin saving your csv files to the database using the absolute path. For example you would enter the path below after choosing the Import CSV file action (Action-1)
``` bash
     /app/data/filename.csv
```
 6. You can then query your CSV file following the instructions prompted to you. Remember, any time 
 you need a reminder of the availiable actions, enter 5 when promted to select an action.

 7. After exiting the application, if you want to start up the same container (which you probably will want to do), run the following command and then repeat step 4.
``` bash
     docker start yourcontainername
```
 8. Additionally, if you want to run a shell inside the container you can use the following command.
``` bash
    docker exec -it yourcontainername bash
```
    This will allow you to interact with the actual application shell which contains the data folder.
    If you ever want to make sure you copied files over correctly you can use this command and cd into the data folder and view all of the csv files you have using the ls command once inside the folder. 