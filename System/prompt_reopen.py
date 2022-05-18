""" ---Importing Modules--- """
from kivy.lang import Builder # For the kv file 
from kivy.app import App # For the main app
from kivy.uix.widget import Widget # For  the widgets
from os import _exit # For the exit function
from functools import cache # For the cache function

""" ---Setting Class For Executing The Programs--- """
Builder.load_file('Kivy_Files\\Reopen.kv') # Loading the kv file

class Main(Widget): # The main class

    @cache  # Caching the function

    def reopen(self): # The reopen function

        _exit(0) # Exiting the app


class Reopen(App): # The launcher class

    @cache  # Caching the function

    def build(self): # The build function

        self.icon = 'Img\Icon.ico' # Setting the icon

        self.title = 'Reopen' # Setting the title

        return Main() # Returning the main class


if  __name__ == '__main__': # If the program is called directly

    Reopen().run() # Running the main app

""" --- End Of App ---"""
