""" ---Importing Modules--- """
from os import chdir, system # For the chdir and system functions
from functools import cache # For caching the functions


""" ---Setting Class For Executing The Programs--- """
class Run_App:  # Class for running the app

    @cache  # Caching the function

    def __int__(self, path, file):  # Constructor

        self.path = path  # Setting the path

        self.file = file  # Setting the file

    @cache  # Caching the function

    def start_app(self):  # Method for starting the app

        chdir(self.path)  # Changing the directory to the path
        
        system(self.file)  # Running the file


""" --- End Of App ---"""
