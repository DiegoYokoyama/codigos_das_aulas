from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager
from random import randint

class Menu(Screen):
    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.start_btn = Button(text='Jogar', font_size=20)
        self.start_btn.bind(on_press=self.mudar_para_jogo)
        self.leave_btn = Button(text='Sair', font_size=20)
        self.leave_btn.bind(on_press=App.get_running_app().stop)
        layout.add_widget(self.start_btn)
        layout.add_widget(self.leave_btn)
        self.add_widget(layout)

    def mudar_para_jogo(self, *args):
        self.manager.current = 'game'

