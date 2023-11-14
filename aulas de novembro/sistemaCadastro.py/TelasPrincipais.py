from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager
from banco import *

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
        bd = BancoDados()
        
    def TelaEditar(self, *args):
        self.manager.current = 'Editar'
        bd = BancoDados()
    
    def TelaExcluir(self, *args):
        self.manager.current = 'excluir'
        bd = BancoDados()
        
    def TelaRegistro(self, *args):
        self.manager.current = 'Registros'
        bd = BancoDados()
        
