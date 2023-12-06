from Menu import *

class AcerteONumero(Screen):
    def __init__(self, **kwargs):
        super(AcerteONumero, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.resultado_lbl = Label(text='Digite um número entre 1 e 100',
                                  font_size=20, size_hint_y=None, height=50)
        self.input_txt = TextInput(multiline=False, font_size=20)
        self.enviar_btn = Button(text='Adivinhar', font_size=20,on_press=self.verificar_acerto)
        self.reiniciar_btn = Button(text='Resetar Jogo', font_size=20,on_press=self.reiniciar_game)
        
        self.menu_btn = Button(text='Voltar para o Menu', font_size=20,on_press=self.mudar_para_menu)
        
        layout.add_widget(self.resultado_lbl)
        layout.add_widget(self.input_txt)
        layout.add_widget(self.enviar_btn)
        layout.add_widget(self.reiniciar_btn)
        layout.add_widget(self.menu_btn)  
        self.add_widget(layout)
        self.reiniciar_game()  
        self.cont = 0
    def mudar_para_menu(self, *args):  
        self.manager.current = 'menu_principal'
        
    def reiniciar_game(self, *args):
        self.num = randint(1, 100)
        self.resultado_lbl.text = 'Digite um número entre 1 e 100'
        self.input_txt.text = ''

    def verificar_acerto(self, instance):
        try:
            adivinhar = int(self.input_txt.text)
            self.cont = self.cont + 1
            if adivinhar == self.num:
                self.resultado_lbl.text = f'Parabéns! Você acertou! essa e a quantidade utilizada para acertar {self.cont}'
            elif adivinhar < self.num:
                self.resultado_lbl.text = 'O número é maior'
            elif adivinhar > self.num:
                self.resultado_lbl.text = 'O número é menor'
        except ValueError:
            self.resultado_lbl.text = 'Por favor, insira um número válido.'