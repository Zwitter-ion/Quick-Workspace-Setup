""" ---Importing Modules--- """
import os #For directory changing

""" ---Setting Class For Executing The Programs--- """
class Run_App(): #Class for running the app
    def __int__(self, path, file): #Constructor
        self.path = path #Setting the path
        self.file = file #Setting the file
    def start_app(self): #Method for starting the app
        os.chdir(self.path) #Changing the directory to the path
        os.system(self.file) #Running the file