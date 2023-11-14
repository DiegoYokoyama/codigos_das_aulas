from TelasPrincipais import *

class RegistroCadastro(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical')
        self.lbl_registro_cadastre = Label (text =' Registro Usuario ',font_size=40)
        self.lbl_registro_verificar = Label(text='Digite o ID que vc quer verificar',font_size=20, size_hint_y=None, height=50)
        self.txt_id_registro = TextInput(multiline=False, font_size=20,hint_text = 'Digite o ID que vc quer verificar: ')
        self.txt_nome_registro = TextInput(multiline=False, font_size=20)
        self.txt_email_registro = TextInput(multiline=False, font_size=20)
        self.btn_verificar_registro = Button(text='verificar', font_size=20,on_press=self.RegistroVerifica)
        self.btn_registro_voltar = Button(text='voltar', font_size=20,on_press=self.RegistroVoltar)
        
        layout.add_widget(self.lbl_registro_cadastre)
        layout.add_widget(self.lbl_registro_verificar)
        layout.add_widget(self.txt_id_registro)
        layout.add_widget(self.txt_nome_registro)
        layout.add_widget(self.txt_email_registro)
        layout.add_widget(self.btn_verificar_registro)
        layout.add_widget(self.btn_registro_voltar)
        self.add_widget(layout)
        
        
    def RegistroVerifica (self, *args):
        self.manager.current = 'verificaRegistro'
        
    def RegistroVoltar (self, *args):
        self.manager.current = 'VoltarRegistro'
        bd = BancoDados()
        bd.fechar_conexao()