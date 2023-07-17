import os
from Banco import *

while True:
    print('Bem Vindo ao Banco')
    menu= int(input('[1]-Funcionario\n[2]-cliente\n[0]-sair\nDigite aqui: '))
    if menu == 1:
        print("[1]-Adicionar Funcionario\n[2]-Excluir Funcionário\n[3]-Adicionar salario de funcionario\n[0]Sair")
        menu_fun = int(input("Digite a função desejada: "))
        if menu_fun == 1:
            nome = input("Digite o nome: ")
            cpf = input("Digite CPF: ")
            idade = int(input("Digite sua idade: "))
            endereco = input("Digite o endereço: ")
            email = input("Digite o email: ")
            tel = int(input("Digite o telefone: "))
            gen = input("Digite o seu Gênero Sexual: ")
            matricula_fun = int(input("Crie a matricula de funcionário: "))
            senha = input("Crie uma senha de funcionario ")
            func_dados = Funcionario(matricula_fun,nome,idade,senha,cpf,endereco,tel,email,gen)
            print("Cadastro de Funcionário realizado com sucesso!")
            os.system('pause')
            os.system('cls')
        
        elif menu_fun == 2:
            print("------------------FUNÇÃO EXCLUIR FUNCIONÁRIO------------------")
            matricula = int(input("Digite o seu numero de matricula para acessar: "))
            senha_dig = input("Digite a sua senha para poder acessar: ")
            func_dados.excluirFuncionario(matricula,senha_dig)
            nome_fun = input("Digite o nome do funcionário(PARA EXCLUIR): ")
            cpf_fun = input("Digite o CPF do funcionário que deseja excluir: ")
            print("------------------Funcionário Excluido com sucesso------------------") 
            os.system('pause')
            os.system('cls')

        elif menu_fun == 3:
            print("------------------FUNÇÃO PAGAMENTO------------------")
            nome_fun = input("Digite o nome do funcionário: ")
            matricula_fun = int(input("Digite a matricula do funcionário: "))
            salario = float(input("Digite o valor de salário do funcionario: "))
            pagamento_fun = Pagamento(nome_fun,matricula_fun,salario)
            os.system('pause')
            os.system('cls')

        elif menu_fun == 0:
            break

    elif menu == 2:

        print("---------------SEÇÃO DE CLIENTE---------------")
        print("[1]-Cadastro Cliente\n[2]-Deposito\n[3]-Saque\n[4]-Saldo\n[0]-Sair")

        menu_client = int(input("Digite a função desejada: "))
        
        if menu_client == 1:
            
            nome_client = input("Digite o nome do cliente: ")
            cpf_client = input("Digite o CPF do cliente: ")
            idade_client = int(input("Digite a sua idade: "))
            endereco_client = input("Digite o seu endereço: ")
            email_client = input("Digite o seu email: ")
            tel_client = int(input("Digite o seu telefone: "))
            gen_client = input("Digite o seu Genêro Sexual: ")
            saldo_client = float(input("Digite o seu saldo no banco: "))
            senha_client = input("Crie umna senha para acessar o banco: ")
            client_dados = client(saldo_client,nome_client,idade_client,senha_client,cpf_client,endereco_client,tel_client,email_client,gen_client)
            print("---------------Cadastro Realizado com sucesso!---------------")
            os.system('pause')
            os.system('cls')
        
        elif menu_client == 2: 

            print("---------------FUNÇÃO DE DEPOSITO---------------")
            valor = float(input("Digite o valor para depositar: "))
            client_dados.deposito(valor)
            os.system('pause')
            os.system('cls')
        
        elif menu_client == 3: 

            print("---------------FUNÇÃO DE SAQUE---------------")
            senha = input("Digite a sua senha para entrar")
            valor = float(input("Digite o valor para saque: "))
            client_dados.sacar(senha,valor)
            os.system('pause')
            os.system('cls')
        
        elif menu_client == 4:

            print("---------------FUNÇÃO DE SALDO---------------")
            senha = input("Digite a sua senha para entrar")
            os.system('pause')
            os.system('cls')
        
        elif menu_client == 0:
            break



