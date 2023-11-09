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
        self.btn_sair = Button(text='Sair', font_size=20,on_press=App.get_running_app().stop)
        
        layout.add_widget(self.lbl_sistema_Cadastro)
        layout.add_widget(self.btn_cadastrar)
        layout.add_widget(self.btn_editar)
        layout.add_widget(self.btn_excluir)
        layout.add_widget(self.btn_sair)
        self.add_widget(layout)
        
    def TelaCadastro(self, *args):
        self.manager.current = 'Cadastrar'
    
    def TelaEditar(self, *args):
        self.manager.current = 'Editar'
    
    def TelaExcluir(self, *args):
        self.manager.current = 'excluir'
        
        
        
class TelaDeCadastro(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical')
        self.lbl_cadastre = Label (text =' Cadastre seu Usuario ',font_size=40)
        self.nome_txt = TextInput(multiline=False, font_size=20, hint_text = 'Digite seu nome: ')
        self.email_txt = TextInput(multiline=False, font_size=20, hint_text = 'Digite seu Email: ')
        self.senha_txt = TextInput(multiline=False, font_size=20, hint_text = 'Digite sua senha: ',password = True)
        self.btn_cadastra_user = Button(text='Cadastrar User', font_size=20,on_press=self.user_cadastrado)
        self.btn_Cadastro_voltar = Button(text='voltar', font_size=20,on_press=self.voltarCadastro)
        
        layout.add_widget(self.lbl_cadastre)
        layout.add_widget(self.nome_txt)
        layout.add_widget(self.email_txt)
        layout.add_widget(self.senha_txt)
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
        self.verificar_lbl = Label(text='Digite o nome que vc quer editar',font_size=20, size_hint_y=None, height=50)
        self.nome_verificar_txt = TextInput(multiline=False, font_size=20, hint_text = 'Digite seu nome: ')
        self.email_verificar_txt = TextInput(multiline=False, font_size=20, hint_text = 'Digite seu Email: ')
        self.senha_verificar_txt = TextInput(multiline=False, font_size=20, hint_text = 'Digite sua senha: ',password = True)
        self.btn_editar_user = Button(text='Editar User', font_size=20,on_press=self.editarUser)
        self.btn_editar_voltar = Button(text='voltar', font_size=20,on_press=self.voltarEditar)

        
        layout.add_widget(self.lbl_editar_cadastre)
        layout.add_widget(self.verificar_lbl)
        layout.add_widget(self.nome_verificar_txt)
        layout.add_widget(self.email_verificar_txt)
        layout.add_widget(self.senha_verificar_txt)
        layout.add_widget(self.btn_editar_user)
        layout.add_widget(self.btn_editar_voltar)
        self.add_widget(layout)
        
    def voltarEditar(self, *args):
        self.manager.current = 'VoltarEditar'
    
    def editarUser(self, *args):
        self.manager.current = 'Editar User'
    
    '''def verificar_nome(self, instance):
        try:
            verificarNome = self.nome_verificar_txt
            if verificarNome == self.nome_verificar_txt:
                self.verificar_lbl.text = 'Nome valido '
            elif verificarNome != self.nome_verificar_txt:
                self.verificar_lbl.text = ' nome invalido'
        except ValueError:
            self.verificar_lbl.text = 'Por favor, insira um nome valido.'   '''
    
    
class Telaexcluir(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical')
        self.lbl_editar_cadastre = Label (text =' Excluir Usuario ',font_size=40)
        self.verificar_lbl = Label(text='Digite o nome que vc quer excluir',font_size=20, size_hint_y=None, height=50)
        self.btn_excluir_user = Button(text='Excluir User', font_size=20,on_press=self)
        self.btn_excluir_voltar = Button(text='voltar', font_size=20,on_press=self)
        
        layout.add_widget(self.lbl_editar_cadastre)
        layout.add_widget(self.verificar_lbl)
        layout.add_widget(self.btn_excluir_user)
        layout.add_widget(self.btn_excluir_voltar)
        self.add_widget(layout)
        
    def ExcluirUser (self, *args):
        self.manager.current = 'ExcluirUser' 
        
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
        
        gerenciar_tela.add_widget(Telaexcluir(name='excluir'))
        
        return gerenciar_tela


if __name__ == '__main__':
    main().run()






