""" ---Importing The Modules--- """
import os  # For directory changing
from System.Brain import Run_App  # For running the app
from functools import cache # For caching the functions


""" ---Asking the user which mode to start--- """
class Start_App():  # Class for starting the app

    @cache  # Caching the function

    def verify_data_files(self,mode):  # Method for verifying the data files

        mode_name =  mode # Asking the user for the mode name

        global path  # Setting the path as global

        path = os.getcwd() + f'\Data\\{mode_name}.qes'  # Setting the path

        if not os.path.exists(path):  # If the path doesn't exist

            print("FILE DOESN'T EXIST!!!")  # Printing the message

            os._exit(0)  # Exiting the program

        else:  # If the path exists

            with open(path, 'r') as data_file:  # Opening the data file

                info = data_file.readlines()  # Reading the data file

                for apps in info:  # For each app in the data file

                    apps = apps.split(' | ')  # Splitting the path and file into a list

                    app = Run_App()  # Creating an instance of the Run_App class

                    app.path = apps[0]  # Setting the path

                    app.file = apps[1]  # Setting the file

                    app.start_app()  # Running the app

                os._exit(0) # Exiting the program


""" --- End Of App ---"""
