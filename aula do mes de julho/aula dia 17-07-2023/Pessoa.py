class Pessoa():


    def __init__(self,nome,idade,endereco,cidade,estado):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado

    
    def relatorio(self):
        print('Nome.........',self.nome)
        print('idade........',self.idade)
        print('endereco.....',self.endereco)
        print('cidade.......',self.cidade)
        print('estado.......',self.estado)