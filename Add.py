""" ---Importing Modules--- """
from tkinter import filedialog # For the file dialog
from functools import cache # For the cache function

""" ---Setting Class For Executing The Programs--- """
class add_mode(): # The add mode class
    
    @cache # Caching the function
    
    def add_programs(self): # The add programs function

        file_and_path = filedialog.askopenfilename() # Getting the file and path

        self.file = file_and_path.split('/')[-1] # Getting the file name

        self.path = file_and_path.split(self.file)[0] # Getting the path


if __name__ == '__main__': 
    add_mode = add_mode()
    add_mode.add_programs()

""" --- End Of App ---"""
