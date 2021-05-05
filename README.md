# Python Lab Exercises
## Setup
1. Install python from [python.org](https://python.org/downloads). 
    - This lab requires python version 3.6+, but download the latest recommended version of Python 3
2. Copy the ACE Labs folder where you want to store the labs
3. Open the Command Prompt and navigate into the ACE Labs folder. There should be 5 items in this directory:
    - Labs (folder)
    - Tests (folder)
    - .gitignore (file)
    - README.md (file)
    - requirements.txt (file)
4. Run ```python -m venv venv``` to set up your virtual environment.
5. Activate your virtual environment. The command may vary based on whether you're running Mac, Linux, or Windows.
    - Windows: ```.\venv\Scripts\activate```
    - MacOS/Linux: ```source venv/bin/activate```
6. Install the modules required for these labs: ```pip install -r requirements.txt```
7. Run the following. If all tests pass, you have completed the setup and can proceed to Lab 1
   - ```python -m unittest Tests/test_setup.py -v```