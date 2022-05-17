""" ---Importing Modules--- """
from Add import add_mode  # For the add mode function
from kivy.app import App  # For the main app
from kivy.uix.widget import Widget  # For the widgets
from kivy.lang import Builder  # For the kv file
from kivy.uix.label import Label  # For the labels
from kivy.uix.button import Button  # For the buttons
from kivy.uix.textinput import TextInput  # For the text inputs
import os  # For the file system and other stuff
from functools import cache  # For the cache function


""" ---Setting Class For Executing The Programs--- """
Builder.load_file('Add_gui.kv')  # Loading the kv file

class add(Widget):  # The main class

    @cache # Caching the function

    def __init__(self, **kwargs):  # The init function

        super(add, self).__init__(**kwargs)  # Calling the init function of the parent class

        self.mode_name = None # Creating the mode name

        self.path_text = None # Creating the path text

        self.file_text = None # Creating the file text  

        self.data = None # Creating the data

        self.path = None # Creating the path

        self.file = None # Creating the file

        self.data_list = []  # Creating a list for the data

    @cache  # Caching the function

    def press_add_mode(self):  # The add mode function

        Add_mode = add_mode()  # Calling the add mode function

        Add_mode.add_programs()  # Calling the add programs function

        self.file = Add_mode.file  # Getting the file

        self.path = Add_mode.path  # Getting the path

        self.data = f'{self.path} | {self.file}'  # Creating the data

        self.file_text = Label(text=self.file, color=[0.41, 0.42, 0.74, 1], font_size=20,
                               font_name='Comic')  # Creating the file text

        self.path_text = Label(text=self.path, color=[0.41, 0.42, 0.74, 1], font_size=20,
                               font_name='Comic')  # Creating the path text

        self.ids.grid.add_widget(self.path_text)  # Adding the path text to the grid

        self.ids.grid.add_widget(self.file_text)  # Adding the file text to the grid

        self.data_list.append(self.data)  # Appending the data to the list

        if len(self.data_list) == 0:  # If the list is empty

            App.get_running_app().root.ids.save.disabled = True  # Disabling the save button

        else:  # If the list is not empty

            App.get_running_app().root.ids.save.disabled = False  # Enabling the save button

    @cache  # Caching the function

    def save_data(self):  # The save data function

        self.ids.grid.clear_widgets()  # Clearing the grid

        self.ids.buttons.clear_widgets()  # Clearing the buttons

        self.ids.title.clear_widgets()  # Clearing the title

        self.ids.title.add_widget(Label(text='Add Mode Name', color=[0.41, 0.42, 0.74, 1], font_size=30,
                                        font_name='Comic'))  # Adding the title

        self.ids.grid.add_widget(Label(text='Enter a name for the mode', color=[0.41, 0.42, 0.74, 1], font_size=20,
                                       font_name='Comic'))  # Adding the label

        self.mode_name = TextInput(text='Enter Name Here', multiline=False, size_hint=(1, .1),
                                   pos_hint={'center_x': .5, 'center_y': .5})  # Creating the text input

        self.ids.grid.add_widget(self.mode_name)  # Adding the text input to the grid

        self.ids.buttons.add_widget(
            Button(text='Save', size_hint_x=1, font_name='Comic', background_normal='', color=[0.41, 0.42, 0.74, 1], font_size=20, on_press=lambda x: self.save_to_file()))  # Adding the save button to the buttons

    @cache  # Caching the function

    def save_to_file(self):  # The save to file function

        with open('Data//Mode_list.qes', 'a') as file:  # Opening the file

            mode_name = self.mode_name.text  # Getting the mode name

            file.write(f'{mode_name}\n')  # Writing the mode name to the file

            print('added name')  # Printing the added name

        with open(f'Data//{mode_name}.qes', 'a') as data_file:  # Opening the file

            for items in self.data_list:  # For each item in the list

                data_file.write(f'{items}\n')  # Writing the data to the file

        os.system('prompt_reopen.py')  # Reopening the program

        os._exit(0)  # Exiting the program


class Add_Mode(App):  # The load class

    @cache  # Caching the function

    def build(self):  # The build function

        self.icon = 'Img\Icon.ico'  # Setting the icon

        return add()  # Returning the add class


if __name__ == '__main__': # If the program is run directly

    Add_Mode().run() # Running the program


""" --- End Of App ---"""
