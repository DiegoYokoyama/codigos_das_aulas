from TelasPrincipais import *
from RegistrarCadastro import *
from TelaDeCadastro import *
from TelaEditar import *
from TelaExcluir import *
class main(App):
    def build(self):
        gerenciar_tela = ScreenManager()
        gerenciar_tela.add_widget(TelasPrincipais(name='inicio'))
        gerenciar_tela.add_widget(TelaDeCadastro(name='Cadastrar'))
        gerenciar_tela.add_widget(TelasPrincipais(name='Cadastrar User'))
        gerenciar_tela.add_widget(TelasPrincipais(name = 'VoltarCadastro'))
        
        gerenciar_tela.add_widget(TelaEditar(name='Editar'))
        gerenciar_tela.add_widget(TelaEditar(name='Editar User'))
        gerenciar_tela.add_widget(TelasPrincipais(name = 'VoltarEditar'))
        
        gerenciar_tela.add_widget(TelaExcluir(name='excluir'))
        gerenciar_tela.add_widget(TelaExcluir(name='ExcluirUser'))
        gerenciar_tela.add_widget(TelasPrincipais(name='VoltarExcluir'))
        
        gerenciar_tela.add_widget(RegistroCadastro(name='Registros'))
        gerenciar_tela.add_widget(RegistroCadastro(name='verificaRegistro'))
        gerenciar_tela.add_widget(TelasPrincipais(name='VoltarRegistro'))
        
        
        return gerenciar_tela


if __name__ == '__main__':
    main().run()