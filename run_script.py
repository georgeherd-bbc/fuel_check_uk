#script to run python script and load dependent modules and imports from a requirements.txt file

import subprocess
import os
import sys

def run_command(command):
    """Run a shell command and ensure it completes successfully."""
    result = subprocess.run(command, shell=True, check=True, text=True)
    return result

def install_requirements():
    """Install packages from requirements.txt if the file exists."""
    requirements_file = 'requirements.txt'
    if os.path.exists(requirements_file):
        print(f"Installing requirements from {requirements_file}...")
        run_command(f"{sys.executable} -m pip install -r {requirements_file}")
    else:
        print(f"{requirements_file} does not exist. Skipping package installation.")

def execute_script(script_name):
    """Execute the given Python script."""
    if os.path.exists(script_name):
        print(f"Executing script {script_name}...")
        run_command(f"{sys.executable} {script_name}")
    else:
        print(f"Script {script_name} does not exist. Aborting execution.")

if __name__ == "__main__":
    # Ensure the script name is passed as an argument
    if len(sys.argv) != 2:
        print("Usage: python run_script.py <script_name>")
        sys.exit(1)

    script_name = sys.argv[1]

    try:
        # Step 1: Install requirements
        install_requirements()
        
        # Step 2: Execute the script
        execute_script(script_name)

        print("Script executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the command: {e}")
        sys.exit(e.returncode)