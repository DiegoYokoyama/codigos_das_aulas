from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager

class WelcomeScreen(Screen):
    def __init__(self, **instance):
        super().__init__(**instance)
        layout = BoxLayout(orientation='vertical')
        label = Label(text="Bem-vindo ao Jogo")
        button = Button(text="Jogar")
        button.bind(on_press=self.switch_to_info)
        layout.add_widget(label)
        layout.add_widget(button)
        self.add_widget(layout)

    def switch_to_info(self, instance):
        self.manager.current = 'jogo'

class InfoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text="")
        text_input = TextInput(hint_text='Digite um número')
        button = Button(text="Verificar")
        button.bind(on_press=self.switch_to_welcome)
        layout.add_widget(label)
        layout.add_widget(text_input)
        layout.add_widget(button)
        self.add_widget(layout)

    def switch_to_welcome(self, instance):
        self.manager.current = 'começo'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='começo'))
        sm.add_widget(InfoScreen(name='jogo'))
        return sm