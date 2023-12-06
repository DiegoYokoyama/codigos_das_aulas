from TelasPrincipais import *
class TelaExcluir(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical')
        self.lbl_excluir_cadastre = Label (text =' Excluir Usuario ',font_size=40)
        self.lbl_excluir_verificar = Label(text='Digite o nome que vc quer excluir',font_size=20, size_hint_y=None, height=50)
        self.txt_id_excluir = TextInput(multiline=False, font_size=20,input_filter= 'int', hint_text = 'Digite o Id ')
        #self.txt_nome_excluir = TextInput(multiline=False, font_size=20)
        #self.txt_email_excluir = TextInput(multiline=False, font_size=20)
        self.btn_excluir_user = Button(text='Excluir User', font_size=20,on_press=self.ExcluirUser)
        self.btn_excluir_voltar = Button(text='voltar', font_size=20,on_press=self.ExcluirVoltar)
        
        layout.add_widget(self.lbl_excluir_cadastre)
        layout.add_widget(self.lbl_excluir_verificar)
        layout.add_widget(self.txt_id_excluir)
        #layout.add_widget(self.txt_nome_excluir)
        #layout.add_widget(self.txt_email_excluir)
        layout.add_widget(self.btn_excluir_user)
        layout.add_widget(self.btn_excluir_voltar)
        self.add_widget(layout)
        
    def ExcluirUser (self, *args):
        
        id_nome = self.txt_id_excluir
        bd = BancoDados()
        bd.Excluir_valores(id_nome)
        bd.fechar_conexao()
        self.manager.current = 'ExcluirUser' 
        
    def ExcluirVoltar (self, *args):
        bd = BancoDados()
        bd.fechar_conexao()
        self.manager.current = 'VoltarExcluir'