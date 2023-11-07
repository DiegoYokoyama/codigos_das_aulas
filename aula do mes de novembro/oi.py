import kivy 

from kivy.app import App
from kivy.uix.label import Label

class Test01(App):
    def build(self):
        lbl_test=Label(text = 'testando')
        
        return lbl_test

if __name__=="__main__":
    Test01().run()