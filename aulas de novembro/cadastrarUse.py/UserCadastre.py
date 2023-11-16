import os
import mysql.connector

class BancoSQL:
    def __init__(self):
        self.UserCadastro = mysql.connector.connect ( 
        host = '10.28.1.135',
        database = 'UserCadastro',
        user = 'Toshio',
        password = 'DiegoToshio.2003'
        )
        
    def conectar(self):
        if self.UserCadastro.is_connected():
            database_informacao = self.UserCadastro.get_server_info()
            print(f"Conectado ao Banco de Dados = {database_informacao}")
            
        self.cursor = self.UserCadastro.cursor()
        
    def Registrar_conta(self,nome, cpf, endereco,sexo,idade,rg,email,cidade,estadoCivil,escolaridade):
        today = "insert into Usuario (nome, cpf, endereco,sexo,idade,rg,email,cidade,estadoCivil,escolaridade) values (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s)"
        values = (nome, cpf, endereco,sexo,idade,rg,email,cidade,estadoCivil,escolaridade)

        self.cursor.execute(today, values)
        self.UserCadastro.commit()
        print(self.cursor.rowcount, "registro(s) inserido(s).")
        
    def conexao_fechar(self):
        if self.UserCadastro.is_connected():
            self.UserCadastro.close()
            print("Conexão encerrada")
            print("-=" * 20)
            
while True:

    
    try:
        op= int(input('escolha a opiçao\n 1 para cadastro\n 2 para sair\n Digite aqui:'))
        os.system('pause')
        os.system('cls')
    except ValueError:
        os.system('cls')
        print('Digite apenas numeros validos')
        os.system('pause')
        os.system('cls')
       
        
         
    else:

        if op == 1:
            try:
                bd=BancoSQL()
                bd.conectar()
                nome = input('Digite seu nome: ')
                cpf = input('Digite seu cpf: ')
                endereco = input ('Digite seu endereço rua, numero da casa e bairro: ')
                sexo = input(' Digite seu sexo: ')
                idade = int(input('Digite sua idade: '))
                rg = input('Digite seu rg: ')
                email = input('Digite seu email: ')
                cidade = input('Digite sua cidade: ')
                estadoCivil = input ('Digite seu estado civil: ')          
                escolaridade = input ('Digite sua escolaridade: ')  
                os.system('pause')
                os.system('cls')  
            
                bd.Registrar_conta(nome, cpf, endereco,sexo,idade,rg,email,cidade,estadoCivil,escolaridade)
                
            except ValueError:
                os.system('cls')
                print('alguma informação esta errado')
                os.system('pause')
                os.system('cls')
                
        elif op == 2:
            bd=BancoSQL()
            bd.conexao_fechar()
            break
        
        


        
        