from Menu import *

class AcerteONumero(Screen):
    def __init__(self, **kwargs):
        super(AcerteONumero, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.resultado_lbl = Label(text='Digite um número entre 1 e 100',
                                  font_size=20, size_hint_y=None, height=50)
        self.input_txt = TextInput(multiline=False, font_size=20)
        self.submit_btn = Button(text='Adivinhar', font_size=20)
        self.submit_btn.bind(on_press=self.check_guess)
        self.reset_btn = Button(text='Resetar Jogo', font_size=20)
        self.reset_btn.bind(on_press=self.reset_game)
        
        self.menu_btn = Button(text='Voltar para o Menu', font_size=20)
        self.menu_btn.bind(on_press=self.switch_to_menu)  
        
        layout.add_widget(self.resultado_lbl)
        layout.add_widget(self.input_txt)
        layout.add_widget(self.submit_btn)
        layout.add_widget(self.reset_btn)
        layout.add_widget(self.menu_btn)  
        self.add_widget(layout)
        self.reset_game()  

    def switch_to_menu(self, *args):  
        self.manager.current = 'menu_principal'
        
    def reset_game(self, *args):
        self.num = randint(1, 100)
        self.resultado_lbl.text = 'Digite um número entre 1 e 100'
        self.input_txt.text = ''

    def check_guess(self, instance):
        try:
            guess = int(self.input_txt.text)
            if guess == self.num:
                self.resultado_lbl.text = 'Parabéns! Você acertou!'
            elif guess < self.num:
                self.resultado_lbl.text = 'O número é maior'
            elif guess > self.num:
                self.resultado_lbl.text = 'O número é menor'
        except ValueError:
            self.resultado_lbl.text = 'Por favor, insira um número válido.'