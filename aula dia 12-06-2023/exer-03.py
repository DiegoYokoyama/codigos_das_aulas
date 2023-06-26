agenda={}
import os
while True:
    try:
        menu=input(' 1=cadastro\n 2=imprimir\n 0=sair \n escolha: ')
        if menu =='1':
            cpf=int(input('Digite seu cpf ou zero para imprimir: '))
            nome=input('Digite seu nome: ')
            idade=int(input('Digite sua idade: '))
            telefone=int(input('Digite seu telefone: '))
            os.system('pause')
            os.system('cls')
            agenda={cpf:{'nome':nome,'idade':idade,'telefone':telefone}}
            print(agenda)
            os.system('pause')
            os.system('cls')
    except ValueError:
        print('por favor digite numeros inteiro sem ponto, virgula, etc')
        os.system('pause')
        os.system('cls')


