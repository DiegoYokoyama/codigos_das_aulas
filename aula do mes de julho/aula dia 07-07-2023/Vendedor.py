class Vendedor():
    def __init__(self,nome,vendas):
        self.nome=nome
        self.vendas=vendas
    def vendeu(self,vendas):
        print(self.vendas)
    def bateu_meta(self,meta):
        if self.vendas>meta:
            print('Bateu a meta')
        else:
            print('Não bateu a meta')