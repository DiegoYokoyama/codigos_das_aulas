from TelasPrincipais import *

class TelaEditar(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical')
        self.lbl_editar_cadastre = Label (text =' Editar Usuario ',font_size=40)
        self.lbl_editar_verificar = Label(text='Digite o nome que vc quer editar',font_size=20, size_hint_y=None, height=50)
        self.txt_id_verificar = TextInput(multiline=False, font_size=20,input_filter= 'int', hint_text = 'Id: ')
        self.txt_nome_editar = TextInput(multiline=False, font_size=20, hint_text = 'Digite seu nome: ')
        self.txt_email_editar = TextInput(multiline=False, font_size=20, hint_text = 'Digite seu Email: ')
        self.txt_senha_editar = TextInput(multiline=False, font_size=20, hint_text = 'Digite sua senha: ',password = True)
        self.btn_editar_user = Button(text='Editar User', font_size=20,on_press=self.editarUser)
        self.btn_editar_voltar = Button(text='voltar', font_size=20,on_press=self.voltarEditar)

        
        layout.add_widget(self.lbl_editar_cadastre)
        layout.add_widget(self.lbl_editar_verificar)
        layout.add_widget(self.txt_id_verificar)
        layout.add_widget(self.txt_nome_editar)
        layout.add_widget(self.txt_email_editar)
        layout.add_widget(self.txt_senha_editar)
        layout.add_widget(self.btn_editar_user)
        layout.add_widget(self.btn_editar_voltar)
        self.add_widget(layout)
        
    def voltarEditar(self, *args):
        bd = BancoDados()
        bd.fechar_conexao()
        self.manager.current = 'VoltarEditar'
    
    def editarUser(self, *args):
        bd = BancoDados()
        bd.Editar_valores()
        self.manager.current = 'Editar User'