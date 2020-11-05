import subprocess
import os
import sys

## Write assert functions for all to be verified

# ToDo: Make sure to install everything in a virtualenvironment
# def install_requirements():
#     print("Installing Required Packages..........")
#     subprocess.run("pip install django".split(' '))
#     return "done"
urls_constant = """from django.urls import path
from .views import *

urlpatterns = [

]


"""

serializers_constant = """from rest_framework import serializers
from .models import *

"""

admin_initial = """from django.contrib import admin
from .models import * 

"""

def create_new_project_sync_settings(project_name):

    ### adding creator stuff
    with open(os.path.join(os.getcwd(), project_name, project_name, 'settings.py'), 'r') as e:
        settings = e.read()
    #print(settings)
    creator = "'django-admin startproject'"
    substitute_string = "Shounak and Abhishek via script"
    settings = settings.replace(creator, substitute_string)
    #print(settings)
    with open(os.path.join(os.getcwd(), project_name, project_name, 'settings.py'), 'w') as e:
        e.write(settings)

    # handling the include part
    with open(os.path.join(os.getcwd(), project_name, project_name, 'urls.py'), 'r') as e:
        urls = e.read()
    urls = urls.replace("from django.urls import path", "from django.urls import path, include")
    with open(os.path.join(os.getcwd(), project_name, project_name, 'urls.py'), 'w') as e:
        e.write(urls)

    
def create_new_project(project_name):
    print("Creating a new project.....")
    try:
        ## handling project already exists
        if os.path.isdir(os.path.join(os.getcwd(), project_name)):
            print("Project already exists!")
            sys.exit(0)
        cmd = 'source env/bin/activate; django-admin startproject {}'.format(project_name)
        subprocess.run(cmd, shell=True, executable='/bin/bash')
        if os.path.isdir(os.path.join(os.getcwd(), project_name)):
            print("Project successfully created!!!")
            print("Syncing settings......")
            ## syncing the settings to include the new app in installed app
            create_new_project_sync_settings(project_name)
            print("Settings successfully synced!!")
        else:
            print("Not working, unable to create project!")
        #subprocess.run("django-admin startproject {}".format(project_name).split(' '))
    except Exception as e:
        print(e)

def create_new_settings_config(project_name, app_name):
    ### setting config to add new app to installed apps
    with open(os.path.join(os.getcwd(), project_name, project_name, 'settings.py'), 'r') as e:
        settings = e.read()
    #print(settings)
    installed_apps = settings.find('INSTALLED_APPS')
    last_bracket = settings.find(']', installed_apps)
    #print(installed_apps)
    #print(last_bracket)
    substitute_string = "\t'{}',\n".format(app_name)+']'
    settings = settings[:last_bracket] + substitute_string + settings[last_bracket+1:]
    with open(os.path.join(os.getcwd(), project_name, project_name, 'settings.py'), 'w') as e:
        e.write(settings)


def create_new_app(project_name, app_name):
    if not os.path.isdir(os.path.join(os.getcwd(), project_name)):
        print("Project does not exist! Create one")
        sys.exit(0)
    if os.path.isdir(project_name):
        if os.path.isdir(os.path.join(os.getcwd(), project_name, app_name)):
            print("App with same name already exists!!")
            sys.exit(0)
        print("Creating a new app for the existing project.....")
        #os.chdir(project_name)
        cmd = 'source env/bin/activate;cd {};django-admin startapp {}'.format(project_name, app_name)
        subprocess.run(cmd, shell=True, executable='/bin/bash')
        #subprocess.run("django-admin startapp {}".format(app_name).split(' '))
        #os.chdir('..')
        if os.path.isdir(os.path.join(os.getcwd(), project_name, app_name)):
            print("App successfully created!!!")
            print("Proceeding to sync settings......")
            create_new_settings_config(project_name, app_name)
            print("Project synced successfully!!")
            cmd = 'cd {}/{};touch urls.py; cd ../{}'.format(project_name, app_name, project_name)
            subprocess.run(cmd, shell=True, executable='/bin/bash')
            with open(os.path.join(os.getcwd(), project_name, app_name, 'admin.py'), 'r') as e:
                admin = e.read()
            if len(admin) == 0:
                with open(os.path.join(os.getcwd(), project_name, app_name, 'admin.py'), 'w') as e:
                    e.write(admin_initial)
            else:
                with open(os.path.join(os.getcwd(), project_name, app_name, 'admin.py'), 'w') as e:
                    e.write(admin+"\nadmin.site.register({})".format(app_name))

        else:
            print("App creation function not working")
    else:
        print("Oops project doesn't exist......Create the project first...")


def configuration_for_setting_up_apis(project_name, app_name):
    cmd = 'source env/bin/activate; pip install djangorestframework; pip freeze > requirements.txt'
    subprocess.call(cmd, shell=True, executable='/bin/bash')
    print("Proceeding to sync settings after the installation......")
    create_new_settings_config(project_name, 'rest_framework')
    print("Project synced successfully for drf!!")
    cmd = 'cd {}/{};touch serializers.py; touch permissions.py'.format(project_name, app_name)
    subprocess.run(cmd, shell=True, executable='/bin/bash')
    
    with open(os.path.join(os.getcwd(), project_name, app_name, 'urls.py'), 'r') as e:
        urls = e.read()
    if len(urls) == 0:
        with open(os.path.join(os.getcwd(), project_name, app_name, 'urls.py'), 'w') as e:
            e.write(urls_constant)
    
    
    with open(os.path.join(os.getcwd(), project_name, app_name, 'serializers.py'), 'r') as e:
        serializers = e.read()
    if len(serializers) == 0:
        with open(os.path.join(os.getcwd(), project_name, app_name, 'serializers.py'), 'w') as e:
            e.write(serializers_constant)
    else:
        pass

def add_url_to_urlpatterns(path, line):
    with open(path, 'r') as e:
        urls = e.read()

    urlpatterns = urls.find('urlpatterns')
    last_bracket = urls.find(']', urlpatterns)
    
    substitute_string = line
    urls = urls[:last_bracket] + substitute_string + urls[last_bracket+1:]
    with open(path, 'w') as e:
        e.write(urls+'\n]')
        print("Successfully added app urls to root url!!")


def add_views_initial_config_to_views(project_name, app_name, ):
    with open(os.path.join(os.getcwd(), project_name, app_name, 'views.py'), 'r') as e:
        views = e.read()
    
    substitute_string = """from rest_framework.generics import(
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
    )
from .serilizers import *


    """
    with open(os.path.join(os.getcwd(), project_name, app_name, 'views.py'), 'w') as e:
        e.write(substitute_string)
        print("Successfully added initial views")

#install_requirements()
# create_new_project('new')
# create_new_app('new', 'supernew1')
# configuration_for_setting_up_apis('new', 'supernew1')
# add_url_to_urlpatterns(os.path.join(os.getcwd(), 'new', 'new', 'urls.py'), '\tpath("home/", include("supernew1.urls")')
# add_views_initial_config_to_views('new', 'supernew1')