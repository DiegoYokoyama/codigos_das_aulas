from Pessoa import *


class Professor(Pessoa):
    def __init__(self,salario,nome,idade,endereco,cidade,estado):
        super().__init__(nome,idade,endereco,cidade,estado)
        self.salario = salario
        print('---------------------------')
        print('peja bem vindo querido professor!!!!')
        super().relatorio()
        print('Salario: ',self.salario)
        print('---------------------------')

        
