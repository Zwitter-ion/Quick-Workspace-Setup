from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.button import Button

Builder.load_file('Core.kv')


class BakeRecipes(Widget):
    def __init__(self, **kwargs):
        super(BakeRecipes, self).__init__(**kwargs)

        

        with open('Data\\Mode_list.qes', 'r') as modes:
            self.modes = modes.read().splitlines()

            for i in self.modes:  # assuming you need to create 5 buttons
                self.button = Button(text=str(i))  # the text on the button
                # self.button.bind(on_press=self.pressed) #when the button is clicked
                self.ids.grid.add_widget(self.button)  # added to the grid

                #     self.add_widget(Label(text=f"Error: {e}"))

                # self.add = Button(text="Add Mode", background_color=(10, 10, 0, .75), font_size=30, font_name='Comic', color=(200, 200, 200, 1), size_hint= (0.5, 1))
                # self.add.bind(on_release= lambda x: add_mode())
                # self.add_widget(self.add)


class Quick_Env_Setup(App):
    def build(self):
        return BakeRecipes()


if __name__ == '__main__':
    Quick_Env_Setup().run()
