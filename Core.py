""" ---Importing Modules--- """
import os.path  # For getting the path and exiting the program
from os import chdir, getcwd, _exit, system  # For the chdir and other functions
from kivy.app import App  # For the main app
from kivy.lang import Builder  # For the kv file
from kivy.uix.button import Button  # For the buttons
from kivy.uix.widget import Widget  # For the widgets
from threading import Thread  # For threading
from functools import cache  # For caching
from subprocess import Popen  # For the popen function

""" ---Setting Class For Executing The Programs--- """
Builder.load_file('System\\Kivy_Files\\Core.kv')  # Loading the kv file

class Start_App:  # Class for starting the app

    def __init__(self):
        self.file = None
        self.path = None

    @cache  # Caching the function
    def verify_data_files(self, mode):  # Method for verifying the data files

        mode_name = mode  # Asking the user for the mode name

        global path  # Setting the path as global

        path = getcwd() + f'\Data\\{mode_name}.qws'  # Setting the path

        if not os.path.exists(path):  # If the path doesn't exist

            print("FILE DOESN'T EXIST!!!")  # Printing the message

            _exit(0)  # Exiting the program

        else:  # If the path exists

            with open(path, 'r') as data_file:  # Opening the data file

                info = data_file.readlines()  # Reading the data file

                for apps in info:  # For each app in the data file

                    apps = apps.split(' | ')  # Splitting the path and file into a list

                    self.path = apps[0]  # Setting the path

                    self.file = apps[1]  # Setting the file

                    chdir(self.path)  # Changing the directory to the path

                    Popen(self.file, shell=True)  # Running the file

                _exit(0)  # Exiting the program

class Main(Widget, Thread):  # The main class

    def __init__(self, **kwargs):  # The init function

        super(Main, self).__init__(**kwargs)  # Calling the init function of the parent class

        try:  # Checking if the file exists

            with open('Data\\Mode_list.qws', 'r') as modes:  # Opening the file

                self.modes = modes.read().splitlines()  # Reading the file and splitting it into a list

                for items in self.modes:  # Looping through the list

                    self.button = Button(text=str(items), background_color=(200, 200, 200, 1), background_normal='',
                                         font_name="Comic", font_size=20,
                                         color=[0.41, 0.42, 0.74, 1])  # Creating the button

                    self.button.bind(
                        on_press=lambda x: Start_App().verify_data_files(items))  # when the button is clicked

                    self.ids.grid.add_widget(self.button)  # added to the grid

        except Exception as error:  # If the file doesn't exist

            print(error)  # Printing the error

    @staticmethod
    def add_mode():  # The add mode function

        system('System\\Add_gui.exe')  # Calling the add gui file

        _exit(0)  # Exiting the program


class Quick_Workspace_Setup(App, Thread):  # The launcher class

    def __init__(self): # The init function

        super().__init__() # Calling the init function of the parent class

        self.title = None  # Setting the title to None

        self.icon = None # Setting the icon to None

    def build(self):  # The build function

        self.icon = 'Img\Icon_128.ico'  # Setting the icon

        self.title = 'Quick Workspace Setup'  # Setting the title

        Main().start()  # Starting the main class

        return Main()  # Returning the main class

if __name__ == '__main__':  # If the program is called directly

    Quick_Workspace_Setup().start()  # Running the main app

""" --- End Of App ---"""
