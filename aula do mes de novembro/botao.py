import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class firstBotao(App):
    def build(self):
        layout = BoxLayout(orientation = 'horizontal')
        grid = GridLayout(cols = 1, size_hint = (0.8, 1.0))

        self.text_input = TextInput(text = 'Digite seu Nome', font_size = 12)
        grid.add_widget(self.text_input)

        button1 = Button(text = 'APAGAR')
        button1.bind(on_press = self.erase_name)
        grid.add_widget(button1)

        button2 = Button(text = 'VERIFICAR')
        button2.bind(on_press = self.verify_name)
        grid.add_widget(button2)

        layout.add_widget(grid)

        return layout
    
    def erase_name(self,instance):
        self.text_input.text = ''


    def verify_name(self,instance):
        if self.text_input.text == 'Diego':
            self.text_input.text = 'Toshio'
        else:
            self.text_input.text = 'meu nome'

if __name__=="__main__":
    firstBotao().run()