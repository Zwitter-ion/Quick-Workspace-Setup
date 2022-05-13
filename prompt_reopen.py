from cProfile import run
from time import sleep
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.widget import Widget

Builder.load_file('Reopen.kv')

class Main(Widget):

    def reopen(self):

        exit()


        
        


class Reopen(App):
    def build(self):
        return Main()


if  __name__ == '__main__':
    Reopen().run()