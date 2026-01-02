Guide to running fuel_check_uk from CMD or Terminal

This assumes you have Python installed - this version was compiled for Python 3.10

Download Files from fuel_check_uk repository - and place in the same folder/directory. Make sure the folder name DOES NOT HAVE SPACES in its name - for example: /home/data project will not work - it would need to be /home/data_project

FILES REQUIRED:

* fuel_prices_checker_uk.py
* requirements.txt
* run_script.py

### Set-up virtual environment

This step is optional - but HIGHLY recommended - for running unknown packages

This presumes you have Python 3 installed:

At prompt:

python3 -m venv venv

This is telling python to create a virtual environment venv in a directory called venv

FOR MACOS AND LINUX - at prompt to run the virtual environment:

source venv/bin/activate

FOR WINDOWS - either cmd.exe terminal or Powershell:

In cmd.exe

venv\Scripts\activate.bat

or if using PowerShell

venv\Scripts\Activate.ps1

The prompt should now show (venv) before the username and directory prompt.

At prompt type the following:

python run_script.py fuel_prices_checker_uk.py

This will download all the files it needs to run the main script, then it will run the webscrapper - 

When the script has run its course - it will ask for a folder/directory path input - this is where you will be saving your Excel file. Do not give it a name - just the folder/directory path - so for example /Volumes/hard_drive/data_stories or C:\data_stories

The script will return a message to say if the save has been successful.

Leave virtual environment and delete venv folder
This is important - otherwise, Python commands will continue running in a virtual environment.

At prompt:

deactivate

At prompt - to remove venv folder

rm -r venv

That's it - you should have a new excel spreadsheet with the latest weekly fuel prices for the UK
