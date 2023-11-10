from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager


class TelasPrincipais(Screen):
    def  __init__(self,**kwargs):
        super(TelasPrincipais, self).__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical')
        self.lbl_sistema_Cadastro = Label (text =' Sistema de Cadastro ',font_size=40)
        self.btn_cadastrar = Button(text='Cadastrar', font_size=20,on_press=self.TelaCadastro)
        self.btn_editar = Button(text='Editar Cadastro', font_size=20,on_press=self.TelaEditar)
        self.btn_excluir = Button(text='Excluir Cadastro', font_size=20,on_press=self.TelaExcluir)
        self.btn_registro = Button(text='Registros', font_size=20,on_press=self.TelaRegistro)
        self.btn_sair = Button(text='Sair', font_size=20,on_press=App.get_running_app().stop)
        
        layout.add_widget(self.lbl_sistema_Cadastro)
        layout.add_widget(self.btn_cadastrar)
        layout.add_widget(self.btn_editar)
        layout.add_widget(self.btn_excluir)
        layout.add_widget(self.btn_registro)
        layout.add_widget(self.btn_sair)
        self.add_widget(layout)
        
    def TelaCadastro(self, *args):
        self.manager.current = 'Cadastrar'
    
    def TelaEditar(self, *args):
        self.manager.current = 'Editar'
    
    def TelaExcluir(self, *args):
        self.manager.current = 'excluir'
        
    def TelaRegistro(self, *args):
        self.manager.current = 'Registros'
        
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
        self.manager.current = 'VoltarCadastro'
    
    def user_cadastrado(self, *args):
        self.manager.current = 'Cadastrar User'
        
        
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
        self.manager.current = 'VoltarEditar'
    
    def editarUser(self, *args):
        self.manager.current = 'Editar User'
    
    
    
class TelaExcluir(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical')
        self.lbl_excluir_cadastre = Label (text =' Excluir Usuario ',font_size=40)
        self.lbl_excluir_verificar = Label(text='Digite o nome que vc quer excluir',font_size=20, size_hint_y=None, height=50)
        self.txt_id_excluir = TextInput(multiline=False, font_size=20,input_filter= 'int', hint_text = 'Id: ')
        self.txt_nome_excluir = TextInput(multiline=False, font_size=20, hint_text = 'Digite seu nome: ')
        self.txt_email_excluir = TextInput(multiline=False, font_size=20, hint_text = 'Digite seu Email: ')
        self.btn_excluir_user = Button(text='Excluir User', font_size=20,on_press=self.ExcluirUser)
        self.btn_excluir_voltar = Button(text='voltar', font_size=20,on_press=self.ExcluirVoltar)
        
        layout.add_widget(self.lbl_excluir_cadastre)
        layout.add_widget(self.lbl_excluir_verificar)
        layout.add_widget(self.txt_id_excluir)
        layout.add_widget(self.txt_nome_excluir)
        layout.add_widget(self.txt_email_excluir)
        layout.add_widget(self.btn_excluir_user)
        layout.add_widget(self.btn_excluir_voltar)
        self.add_widget(layout)
        
    def ExcluirUser (self, *args):
        self.manager.current = 'ExcluirUser' 
        
    def ExcluirVoltar (self, *args):
        self.manager.current = 'VoltarExcluir'
        
        
        
class RegistroCadastro(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical')
        self.lbl_registro_cadastre = Label (text =' Registro Usuario ',font_size=40)
        self.lbl_registro_verificar = Label(text='Digite o ID que vc quer verificar',font_size=20, size_hint_y=None, height=50)
        self.txt_id_registro = TextInput(multiline=False, font_size=20,hint_text = 'Digite o ID que vc quer verificar: ')
        self.txt_nome_registro = TextInput(multiline=False, font_size=20)
        self.txt_email_registro = TextInput(multiline=False, font_size=20)
        self.btn_registro_voltar = Button(text='voltar', font_size=20,on_press=self.RegistroVoltar)
        
        layout.add_widget(self.lbl_registro_cadastre)
        layout.add_widget(self.lbl_registro_verificar)
        layout.add_widget(self.txt_id_registro)
        layout.add_widget(self.txt_nome_registro)
        layout.add_widget(self.txt_email_registro)
        layout.add_widget(self.btn_registro_voltar)
        self.add_widget(layout)
        
    def RegistroVoltar (self, *args):
        self.manager.current = 'VoltarRegistro'
        
class main(App):
    def build(self):
        gerenciar_tela = ScreenManager()
        gerenciar_tela.add_widget(TelasPrincipais(name='inicio'))
        gerenciar_tela.add_widget(TelaDeCadastro(name='Cadastrar'))
        gerenciar_tela.add_widget(TelaDeCadastro(name='Cadastrar User'))
        gerenciar_tela.add_widget(TelasPrincipais(name = 'VoltarCadastro'))
        
        gerenciar_tela.add_widget(TelaEditar(name='Editar'))
        gerenciar_tela.add_widget(TelaEditar(name='Editar User'))
        gerenciar_tela.add_widget(TelasPrincipais(name = 'VoltarEditar'))
        
        gerenciar_tela.add_widget(TelaExcluir(name='excluir'))
        gerenciar_tela.add_widget(TelaExcluir(name='ExcluirUser'))
        gerenciar_tela.add_widget(TelasPrincipais(name='VoltarExcluir'))
        
        gerenciar_tela.add_widget(RegistroCadastro(name='Registros'))
        gerenciar_tela.add_widget(TelasPrincipais(name='VoltarRegistro'))
        
        
        return gerenciar_tela


if __name__ == '__main__':
    main().run()






