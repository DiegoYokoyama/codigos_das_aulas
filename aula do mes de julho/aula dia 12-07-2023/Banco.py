class Banco:

    def __init__(self,nome,saldo,cpf,senha):
        self.nome=nome
        self.__saldo=float(saldo)
        self.__cpf=int(cpf)
        self.__senha=senha
    
    def extrato(self,senha):
        if self.__senha ==  senha:
            print('seu saldo: ',self.__saldo)
        else:
            print('senha invalida')
    

    def deposito(self,valor):
        self.valor = valor
        self.__saldo = self.__saldo + valor
        print('o valor que vc colocou: ',valor)
    
        
        

    def sacar(self,senha,valor):
        self.valor = valor
        if valor <= self.__saldo:
            if senha == self.__senha:
                self.__saldo = self.__saldo - valor
                print('o valor que vc sacou: ',valor)
            else:
                print('senha invalida')
        else:
            print('saldo insuficiente')
        
