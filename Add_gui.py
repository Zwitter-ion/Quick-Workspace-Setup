from operator import mod
from re import I
from Add import add_mode
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import os

Builder.load_file('Add_gui.kv')

class add(Widget):

    def __init__(self, **kwargs):
        super(add, self).__init__(**kwargs)
        self.data_list = []

    def press_add_mode(self):
        
        

        Add_mode = add_mode()
        Add_mode.add_programs()
        self.file = Add_mode.file
        self.path = Add_mode.path


        self.data = f'{self.path} | {self.file}'
        self.file_text = Label(text=self.file, color=[0.41, 0.42, 0.74, 1], font_size=20, font_name='Comic')
        self.path_text = Label(text=self.path, color=[0.41, 0.42, 0.74, 1], font_size=20, font_name='Comic')
        self.ids.grid.add_widget(self.path_text)
        self.ids.grid.add_widget(self.file_text)
        self.data_list.append(self.data)

        if len(self.data_list) == 0:
            App.get_running_app().root.ids.save.disabled = True
        else:
            App.get_running_app().root.ids.save.disabled = False

    def save_data(self):
        
        self.ids.grid.clear_widgets()
        self.ids.buttons.clear_widgets()
        self.ids.title.clear_widgets()
        self.ids.title.add_widget(Label(text='Add Mode Name', color=[0.41, 0.42, 0.74, 1], font_size= 30, font_name='Comic'))

        self.ids.grid.add_widget(Label(text='Enter a name for the mode', color=[0.41, 0.42, 0.74, 1], font_size=20, font_name='Comic'))

        self.mode_name = TextInput(text = 'Enter Name Here', multiline=False, size_hint=(1, .1), pos_hint={'center_x': .5, 'center_y': .5})

        self.ids.grid.add_widget(self.mode_name)

        # self.ids.grid.add_widget(Button(text='Cancel', size_hint_x=1,font_name = 'Comic', background_normal = '', color = [0.41, 0.42, 0.74, 1], font_size= 20 ,on_press=lambda x: exit()))

        self.ids.buttons.add_widget(Button(text='Save', size_hint_x = 1,font_name = 'Comic', background_normal = '', color = [0.41, 0.42, 0.74, 1], font_size= 20 ,on_press= lambda x: self.save_to_file()))

    def save_to_file(self):
        with open('Data//Mode_list.qes', 'a') as file:
            mode_name = self.mode_name.text
            file.write(f'{mode_name}\n')
            print('added name')
        with open(f'Data//{mode_name}.qes', 'a') as data_file:
            for items in self.data_list:
                data_file.write(f'{items}\n')


        os.system('prompt_reopen.py')
        
        exit()



class Add_Mode(App):
    def build(self):
        return add()

if __name__ == '__main__':
    Add_Mode().run()