

import kivy
from kivy.app import App
from kivy.uix.label import Label

class HelloWord(App):
    def build(self):
        return Label(text = "hello word!!")
    
if __name__ == '__main__':
        HelloWord().run()    