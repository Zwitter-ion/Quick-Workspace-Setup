from kivy.lang import Builder
from kivy.app import App
from kivy.uix.widget import Widget

Builder.load_string('''
<Main>
    BoxLayout:
        size: root.width, root.height
        orientation: 'vertical'
        spacing: 10
        padding: 30
        id: text
        cols: 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        Label:
            text: 'Please reopen the app for the changes to take effect'
            font_name: "Comic"
            color: [0.41, 0.42, 0.74, 1]
            font_size: 30
        Button:
            text: 'Exit'
            on_press: root.reopen()
            color: [0.41, 0.42, 0.74, 1]
            font_name: 'Comic'
            font_size: 20
        '''
)

class Main(Widget):

    def reopen(self):

        os._exit(0)


class Reopen(App):
    def build(self):
        self.icon = 'Img\Icon.ico'
        return Main()


if  __name__ == '__main__':
    Reopen().run()