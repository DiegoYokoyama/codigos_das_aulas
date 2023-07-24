class Banco():
    

    def __init__(self,nome,idade,senha,cpf,endereco,telefone,email,genero):
        self.nome = nome
        self.idade = idade
        self.__senha = senha
        self.__cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.genero = genero


class client(Banco):


    def __init__(self,saldo,nome,idade,senha,cpf,endereco,telefone,email,genero):
        super().__init__(nome,idade,senha,cpf,endereco,telefone,email,genero)
        self.__saldo = saldo

    def sacar(self,senha,valor):
        self.valor = valor
        if valor <= self.__saldo:
            if senha == self.__senha:
                self.__saldo = self.__saldo - valor
                print("Saque feito com sucesso!")
            else:
                print('Senha inválida')
        else:
            print('Saldo insuficiente')


    def extrato(self,senha):
        if senha == self.__senha:
            print(self.__saldo)
        else:
            print('Senha inválida')


    def deposito(self,valor):
       self.saldo = self.__saldo + valor
       print('Depositado com sucesso')

    
    def saldo(self,senha):
        if senha == self.__senha:
            print("Seu saldo: R$",self.__saldo)
        else: 
            print("Senha inválida")
    
class Funcionario(Banco):


    def __init__(self,matricula_cadastro,nome,idade,senha,cpf,endereco,telefone,email,genero):
        super().__init__(nome,idade,senha,cpf,endereco,telefone,email,genero)
        self.__matricula_cadastro = matricula_cadastro
        self.senha = senha 

    def excluirFuncionario(self,matricula_cadastro,senha):
        if matricula_cadastro == self.__matricula_cadastro and senha == self.senha:
            print('Matricula encontrada')
        else:
            print('Matricula incorreta')
        
        
    def adicionarFuncionario(self,matricula_cadastro,senha):

        if matricula_cadastro == self.__matricula_cadastro and senha == self.senha:
            print('Matricula encontrada')
        else:
            print('Matricula incorreta')


class Pagamento(Funcionario):

    
    def __init__(self,nome_cadastro,matricula_cadastro,salario):
        self.nome_cadastro = nome_cadastro
        self.matricula_cadastro = matricula_cadastro
        self.salario = salario

        print("Salário de Funcionario Registrado!")