import os
from Conta import *


while True:

    try:
        menu=int(input('1-Cadastro\n2-Saque\n3-Extrato\n4-Deposito\n0-Sair\nDigite aqui: '))
        os.system('cls')

    except ValueError:
        os.system('cls')
        print('Digite apenas numeros: ')
        os.system('pause')
        os.system('cls')
    
    else:


        if menu == 1:
            try:
                nome=input('Digite seu nome: ')
                agencia=int(input('Digite sua agencia: '))
                conta=input('Digite sua conta: ')
                telefone=int(input('Digite seu telefone: '))
                saldo=float(input('Digite seu saldo: '))
                cpf=int(input('Digite seu cpf: '))

                os.system('pause')
                os.system('cls')

                client = Conta(nome,agencia,conta,telefone,saldo,cpf)


            except ValueError:
                os.system('cls')
                print('Digite apenas numeros validos, sem ponto, virgula, etc')
                os.system('pause')
                os.system('cls')

        elif menu == 2:
            try:
                valor=float(input('Digite o valor do saque: '))
                client.saque(valor)
                os.system('pause')
                os.system('cls')


            except ValueError:
                os.system('cls')
                print('Digite apenas numeros: ')
                os.system('pause')
                os.system('cls')

        elif menu == 3:
            print('Seu extrato:')
            client.extrato()
            os.system('pause')
            os.system('cls')
    

        elif menu == 4:
            try:
                valor=float(input('Digite o valor que vc quer depositar: '))
                client.deposito(valor)
                os.system('pause')
                os.system('cls')


            except ValueError:
                os.system('cls')
                print('Digite apenas numeros: ')
                os.system('pause')
                os.system('cls')
        

        elif menu == 0:
            break