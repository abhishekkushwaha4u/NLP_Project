import subprocess
import os

path = os.getcwd()
path1 = os.path.join(path, 'env')
def check_virtualenv():
    if os.path.isdir(path1):
        return True
    else:
        return False

def make_virtualenv():
    check_env = check_virtualenv()
    if check_env:
        print("You have an existing env, skipping env creation.....")
    else:
        print("Creating new env.....")
        subprocess.run(["virtualenv" ,"--python=python3","env"])
        print("Successfully created new env!!!")


def install_requirements():
    check_env = check_virtualenv()
    if check_env:
        #subprocess.run(["source","env/bin/activate"])
        if os.path.isfile('requirements.txt'):
            print("Installing requirements.....please wait....")
            cmd = 'source env/bin/activate; pip install -r requirements.txt; pip freeze > requirements.txt'
            subprocess.call(cmd, shell=True, executable='/bin/bash')
            #subprocess.call('pip install -r requirements.txt')
        else:
            print("Need a requirements.txt file to proceed!")
        #subprocess.run("deactivate")
        print("Packages installed and updated with appropriate version numbers!")
    else:
        print("No virtualenv! Make one!")


# make_virtualenv()
# install_requirements()