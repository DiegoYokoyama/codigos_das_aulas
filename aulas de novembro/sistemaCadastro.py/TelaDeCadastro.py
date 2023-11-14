from TelasPrincipais import *
from banco import *
class TelaDeCadastro(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical')
        self.lbl_cadastre = Label (text =' Cadastre seu Usuario ',font_size=40)
        self.txt_nome = TextInput(multiline=False, font_size=20, hint_text = 'Digite seu nome: ')
        self.txt_email = TextInput(multiline=False, font_size=20, hint_text = 'Digite seu Email: ')
        self.txt_senha = TextInput(multiline=False, font_size=20, hint_text = 'Digite sua senha: ',password = True)
        self.btn_cadastra_user = Button(text='Cadastrar User', font_size=20,on_press=self.user_cadastrado)
        self.btn_Cadastro_voltar = Button(text='voltar', font_size=20,on_press=self.voltarCadastro)
        
        layout.add_widget(self.lbl_cadastre)
        layout.add_widget(self.txt_nome)
        layout.add_widget(self.txt_email)
        layout.add_widget(self.txt_senha)
        layout.add_widget(self.btn_cadastra_user)
        layout.add_widget(self.btn_Cadastro_voltar)
        self.add_widget(layout)
    
    def voltarCadastro(self, *args):
        bd = BancoDados()
        bd.fechar_conexao()
        self.manager.current = 'VoltarCadastro'
    
    def user_cadastrado(self, *args):
        
        nome = self.txt_nome.text
        gmail = self.txt_email.text
        senha = self.txt_senha.text
        
        bd = BancoDados()
        bd.Registrar_valores(nome, gmail, senha)
        
        self.manager.current = 'Cadastrar User'