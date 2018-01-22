Health Application

Prerequisites
    GIT is installed and you have the team repository cloned on your local computer.  

Local Environment Setup

    Overview: The next set of steps will walk you through setting up a Python environment on your desktop.  You only need to execute these steps once.  Once completed you will be able to runn the application whenever you'd like.

    Step 1: Install Python 3.6 by downloading from the following website (https://www.python.org/downloads/release/python-364/)

    Step 2: Confirm the installation was successful by opening a command prompt and type "python -V" (without the quotes and a capital V) at the prompt.  This should display a version number and then return you to the C:\ prompt. e.g. "Python 3.6.x"

    Step 3: Install the flask web server by typing the following command into your command prompt "pip install flask" (without the Quotes).  You will see a list of activities occur in the command prompt.  Once complete you will be returned to the C: prompt.

Running the Application

    Step 1: in a command prompt, Navigate to the folder you have cloned the repository to.  The path will be "X\cs633---Term-Project\HealthApp" where X is the path you have cloned the repo.  In my case the path is "C:\Users\Mike\Software\termproject\cs633---Term-Project\HealthApp"

    Step 2: Run the program by typing "python health_application.py" (without the quotes).  Python and flask will start a web server in the command prompt and you will see the command prompt enter a listening mode.  It will say "* Running on http://127.0.0.1:5000/ (press CTRL+C to quit)"  Now you are ready to test the application.

Testing the application

    Step 1: once you have started the web server above.  Open your browser and navigate to http://localhost:5000/ This will open the home route and serve you the current state of the home page.

