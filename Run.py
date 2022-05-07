""" ---Importing The Modules--- """
import os  # For directory changing
from Brain import Run_App  # For running the app

""" ---Setting The Path--- """
path = os.getcwd() + '\Data\Test_infromation.qes'  # Path to the data file

""" ---Running The Apps--- """
with open(path, 'r') as data_file:  # Opening the data file
    info = data_file.readlines()  # Reading the data file
    for apps in info:  # For each app in the data file
        apps = apps.split(' | ')  # Splitting the path and file into a list
        app = Run_App()  # Creating an instance of the Run_App class
        app.path = apps[0]  # Setting the path
        app.file = apps[1]  # Setting the file
        app.start_app()  # Running the app
