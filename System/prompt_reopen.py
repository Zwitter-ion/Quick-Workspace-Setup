""" ---Importing Modules--- """
import time
from kivy.lang import Builder # For the kv file 
from kivy.app import App # For the main app
from kivy.uix.widget import Widget # For  the widgets
from os import _exit # For the exit function
from multiprocessing import Process # For the multiprocessing

""" ---Setting Class For Executing The Programs--- """

start = time.time()

Builder.load_file('Kivy_Files\\Reopen.kv') # Loading the kv file

class Main(Widget): # The main class

    def reopen(self): # The reopen function

        _exit(0) # Exiting the app
        
        


class Reopen(App): # The launcher class

    def build(self): # The build function

        process_reopen = Process(target=Main.reopen)  # Creating a process

        process_reopen.start()  # Starting the process

        process_reopen.join()  # Joining the process


        self.icon = 'Img\Icon.ico' # Setting the icon

        self.title = 'Reopen' # Setting the title

        

        
        return Main() # Returning the main class


if  __name__ == '__main__': # If the program is called directly

    p = Process(Reopen().run()) # Running the main app

    p.start() # Starting the app

    p.join() # Joining the app



""" --- End Of App ---"""
