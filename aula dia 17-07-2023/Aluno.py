from Pessoa import *


class Aluno(Pessoa):
    

    def __init__(self,mensalidade,nome,idade,endereco,cidade,estado):
        super().__init__(nome,idade,endereco,cidade,estado)
        self.mensalidade = mensalidade
        print('---------------------------')
        print('peja bem vindo querido aluno!!!!')
        super().relatorio()
        print('mensalidade: ',self.mensalidade)
        print('---------------------------')