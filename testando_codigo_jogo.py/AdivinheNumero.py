from MainMenu import *

class AdivinheNumero(Screen):
    def __init__(self, **kwargs):
        super(AdivinheNumero, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.result_label = Label(text='Digite um número entre 1 e 100',
                                  font_size=20, size_hint_y=None, height=50)
        self.input_text = TextInput(multiline=False, font_size=20)
        self.submit_button = Button(text='Adivinhar', font_size=20)
        self.submit_button.bind(on_press=self.check_guess)
        self.reset_button = Button(text='Resetar Jogo', font_size=20)
        self.reset_button.bind(on_press=self.reset_game)
        
        self.menu_button = Button(text='Voltar para o Menu', font_size=20)
        self.menu_button.bind(on_press=self.switch_to_menu)  
        
        layout.add_widget(self.result_label)
        layout.add_widget(self.input_text)
        layout.add_widget(self.submit_button)
        layout.add_widget(self.reset_button)
        layout.add_widget(self.menu_button)  
        self.add_widget(layout)
        self.reset_game()  

    def switch_to_menu(self, *args):  
        self.manager.current = 'main_menu'
        
    def reset_game(self, *args):
        self.number = randint(1, 100)
        self.result_label.text = 'Digite um número entre 1 e 100'
        self.input_text.text = ''

    def check_guess(self, instance):
        try:
            guess = int(self.input_text.text)
            if guess == self.number:
                self.result_label.text = 'Parabéns! Você acertou!'
            elif guess < self.number:
                self.result_label.text = 'O número é maior'
            elif guess > self.number:
                self.result_label.text = 'O número é menor'
        except ValueError:
            self.result_label.text = 'Por favor, insira um número válido.'