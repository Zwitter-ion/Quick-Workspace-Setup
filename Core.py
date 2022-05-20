""" ---Importing Modules--- """
from time import time
from kivy.app import App  # For the main app
from kivy.lang import Builder  # For the kv file
from kivy.uix.button import Button  # For the buttons
from kivy.uix.widget import Widget  # For the widgets
from System.Run import Start_App  # For the start app function
from os import system, _exit  # For the exit function and run the command
# from functools import cache # For the cache function
# from numba import vectorize # For the vectorize function

""" ---Setting Class For Executing The Programs--- """
Builder.load_file('System\\Kivy_Files\\Core.kv')  # Loading the kv file

class Main(Widget):  # The main class


    def __init__(self, **kwargs):  # The init function

        super(Main, self).__init__(**kwargs)  # Calling the init function of the parent class

        try:  # Checking if the file exists

            with open('Data\\Mode_list.qes', 'r') as modes:  # Opening the file

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

    def add_mode(self):  # The add mode function

        system('System\\Add_gui.py')  # Calling the add gui file

        _exit(0)  # Exiting the program


class Quick_Workspace_Setup(App):  # The launcher class


    def build(self):  # The build function

        self.icon = 'Img\Icon.ico'  # Setting the icon

        self.title = 'Quick Workspace Setup'  # Setting the title

        return Main()  # Returning the main class


if __name__ == '__main__':  # If the program is called directly

    Quick_Workspace_Setup().run()  # Running the main app

    print(time())  # Printing the time taken to run the program

""" --- End Of App ---"""
