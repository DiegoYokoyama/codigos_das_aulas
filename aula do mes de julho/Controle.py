class Controle():


    def __init__(self,buttons):
        self.buttons=buttons

    def funcao_ligar(self):
        if self.buttons == 1:
            print('esta ligando a tv')

    def funcao_desligar(self):
        if self.buttons == 2:
            print('esta desligando a tv')

    def funcao_aumentar(self):
        if self.buttons == 3:
            print('aumentar o volume da tv')

    def funcao_diminuir(self):
        if self.buttons == 4:
            print('diminuir o volume da tv')

    def funcao_mudar(self):
        if self.buttons == 5:
            print('mudar de canal')