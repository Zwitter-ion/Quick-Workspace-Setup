from Add import add_mode
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

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
        self.file_text = Label(text=self.file, color=[0.41, 0.42, 0.74, 1])
        self.path_text = Label(text=self.path, color=[0.41, 0.42, 0.74, 1])
        self.ids.grid.add_widget(self.path_text)
        self.ids.grid.add_widget(self.file_text)
        self.data_list.append(self.data)

        if len(self.data_list) == 0:
            App.get_running_app().root.ids.save.disabled = True
        else:
            App.get_running_app().root.ids.save.disabled = False

    def save_data(self):
        
        self.ids.grid.clear_widgets()
        self.ids.grid.add_widget(Label(text='Enter a name for the mode', color=[0.41, 0.42, 0.74, 1]))
        self.ids.grid.add_widget(TextInput(text = 'Enter Name Here',multiline=False, size_hint=(1, .1), pos_hint={'center_x': .5, 'center_y': .5}))


class Add_Mode(App):
    def build(self):
        return add()

if __name__ == '__main__':
    Add_Mode().run()