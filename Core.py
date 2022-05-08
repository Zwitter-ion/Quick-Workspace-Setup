""" ---Importing The Module--- """
from operator import le
from kivy.app import App
from Run import Start_App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from Add import add_mode

class Main(GridLayout):

    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        self.padding = 50
        Button.padding = 50
        Button.background_color = (200, 200, 200, .75)
        Button.font_size = 25
        Button.font_name = 'Comic'
        Button.color = (150, 150, 150, 1)
        self.spacing = 5
        with open('Data\\Mode_list.qes', 'r') as num:
            num = num.read().splitlines()
            if len(num) > 100:
                self.cols = 10
            elif len(num) > 90:
                self.cols = 9
            elif len(num) > 80:
                self.cols = 8
            elif len(num) > 70:
                self.cols = 7
            elif len(num) > 60:
                self.cols = 6
            elif len(num) > 50:
                self.cols = 5
            elif len(num) > 40:
                self.cols = 4
            elif len(num) > 30:
                self.cols = 3
            elif len(num) > 20:
                self.cols = 2
            else: 
                self.cols = 1

        try:
            with open('Data\\Mode_list.qes', 'r') as modes:
                self.modes = modes.read().splitlines()

                for items in self.modes:
                    self.items = Button(text=items)
                    self.items.bind(on_release=lambda x: Start_App().verify_data_files(items))
                    self.add_widget(self.items)
                
        except Exception as e:
            e = str(e)
            self.add_widget(Label(text=f"Error: {e}"))
        
        self.add = Button(text="Add Mode", background_color=(10, 10, 0, .75), font_size=30, font_name='Comic', color=(200, 200, 200, 1), size_hint= (0.5, 1))
        self.add.bind(on_release= lambda x: add_mode())
        self.add_widget(self.add)



class Quick_Env_Setup(App):
    def build(self):
        
        return Main()


if __name__ == '__main__':
    Quick_Env_Setup().run()
