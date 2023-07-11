class Conta:


    def __init__(self,nome,agencia,conta,telefone,saldo,cpf):
        self.nome=nome
        self.agencia=int(agencia)
        self.conta=conta
        self.telefone=int(telefone)
        self.saldo=float(saldo)
        self.cpf=int(cpf)
    

    def saque(self,valor):
        self.saldo = self.saldo - valor
        
    def extrato(self):
        print(self.saldo)
    
    def deposito(self,valor):
        self.saldo = self.saldo + valor