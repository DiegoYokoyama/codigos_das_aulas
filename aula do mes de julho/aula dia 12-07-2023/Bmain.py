import os
from Banco import *

while True:
    try:
        menu=int(input('1-cadastro\n2-extrato\n3-deposito\n4-sacar\n0-sair\nDigite aqui: '))

    except ValueError:
        os.system('cls')
        print('Digite apenas numeros inteiros: ')
        os.system('pause')
        os.system('cls')


    if menu == 1:
        try:
            os.system('cls')
            seu_nome=input('Digite seu nome: ')
            seu_saldo=float(input('Digite seu saldo: '))
            seu_cpf=int(input('Digite seu cpf: '))
            sua_senha=input('Digite sua senha: ')
            client = Banco( seu_nome,seu_saldo,seu_cpf,sua_senha)
            os.system('pause')
            os.system('cls')


        except ValueError:
            os.system('cls')
            print('Digite apenas numeros inteiros: ')
            os.system('pause')
            os.system('cls')


    elif menu == 2:
        os.system('cls')
        sua_senha=input('Digite sua senha: ')
        client.extrato(sua_senha)   
        os.system('pause')
        os.system('cls')


    elif menu == 3:
        try:
            os.system('cls')
            valor=float(input('Digite quando vc quer colocar: '))
            client.deposito(valor)
            os.system('pause')
            os.system('cls')
        
        except ValueError:
            os.system('cls')
            print('Digite apenas numeros: ')
            os.system('pause')
            os.system('cls')


    elif menu == 4:
        os.system('cls')
        sua_senha=input('Digite sua senha: ')
        valor=float(input('Digite quando vc quer tirar: '))
        os.system('pause')
        os.system('cls')
        client.sacar(sua_senha,valor)
        os.system('pause')
        os.system('cls')


    elif menu == 0:
        break
        
    



