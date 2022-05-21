""" ---Importing Modules--- """
import time
from kivy.lang import Builder # For the kv file 
from kivy.app import App # For the main app
from kivy.uix.widget import Widget # For  the widgets
from os import _exit # For the exit function
from threading import * # For the threading module

""" ---Setting Class For Executing The Programs--- """

start = time.time()

Builder.load_file('Kivy_Files\\Reopen.kv') # Loading the kv file

class Main(Widget, Thread): # The main class

    def reopen(self): # The reopen function

        _exit(0) # Exiting the app
        
        


class Reopen(App, Thread): # The launcher class

    def build(self): # The build function


        self.icon = 'Img\Icon.ico' # Setting the icon

        self.title = 'Reopen' # Setting the title
        
        Main().start() # Returning the main class

        return Main() # Returning the main class


if  __name__ == '__main__': # If the program is called directly

    Reopen().start() # Running the main app

""" --- End Of App ---"""
