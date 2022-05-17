""" ---Importing Modules--- """
from kivy.lang import Builder # For the kv file 
from kivy.app import App # For the main app
from kivy.uix.widget import Widget # For  the widgets
import os # For the file system and other stuff
from functools import cache # For the cache function

""" ---Setting Class For Executing The Programs--- """
Builder.load_file('Reopen.kv') # Loading the kv file

class Main(Widget): # The main class

    @cache  # Caching the function

    def reopen(self): # The reopen function

        os._exit(0) # Exiting the app


class Reopen(App): # The launcher class

    @cache  # Caching the function

    def build(self): # The build function

        self.icon = 'Img\Icon.ico' # Setting the icon

        return Main() # Returning the main class


if  __name__ == '__main__': # If the program is called directly

    Reopen().run() # Running the main app

""" --- End Of App ---"""
