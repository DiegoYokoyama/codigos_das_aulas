import kivy
from kivy.app import App 
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        label=Label(text = 'funciona')
        
        return label

if __name__=="__main__":
    MyApp().run()