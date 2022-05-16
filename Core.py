from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.button import Button
from Run import Start_App
from kivy.config import Config
import os

Builder.load_file('Core.kv')


class Main(Widget):
    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)


        try:
            with open('Data\\Mode_list.qes', 'r') as modes:
                self.modes = modes.read().splitlines()

                for items in self.modes:  # assuming you need to create 5 buttons
                    self.button = Button(text=str(
                        items), background_color=(200, 200, 200, 1), background_normal='', font_name="Comic", font_size=20, color=[0.41, 0.42, 0.74, 1])  # the text on the button
                    self.button.bind(on_press= lambda x: Start_App().verify_data_files(items)) #when the button is clicked
                    self.ids.grid.add_widget(self.button)  # added to the grid
            
        except Exception as error:
            print(error)

    def add_mode(self):
        os.system('Add_gui.py')
        os._exit(0)

class Quick_Workspace_Setup(App):
    def build(self):
        self.icon = 'Img\Icon.ico'
        return Main()


if __name__ == '__main__':
    Quick_Workspace_Setup().run()
