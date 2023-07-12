class Banco:

    def __init__(self,nome,saldo,cpf,senha):
        self.nome=nome
        self.__saldo=saldo
        self.__cpf=cpf
        self.__senha=senha
    
    def extrato(self,senha):
        if senha ==  self.__senha:
            return self.__saldo
        else:
            print('senha invalida')
    
    