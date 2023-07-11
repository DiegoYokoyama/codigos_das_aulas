import os
from Bola import *


while True:

    try:
        menu=int(input("1-registro\n2-Trocar a cor da bola\n3-Material da bola\n0-Sair\nDigite aqui: "))
        os.system('cls')

    except ValueError:
        os.system('cls')
        print('Digite apenas numeros inteiros')
        os.system('pause')
        os.system('cls')
    
    else:

        if menu == 1:

            cor=input('Digite a cor da bola: ')
            circunferencia=float(input('Digite a circunferencia: '))
            material=input("Digite o material da bola: ")

            os.system('pause')
            os.system('cls')

            ball = Bola(cor,circunferencia,material)

        elif menu == 2:
            corBola=input('Digite uma cor: ')
            ball.TrocarCor(corBola)
            print('Cor trocada para: ',corBola)

            os.system('pause')
            os.system('cls')    

        elif menu == 3:
            materialBola=input("Digite o material da bola: ")
            ball.MaterialTrocar(materialBola)
            print('A troca de material da bola foi para: ',materialBola)

            os.system('pause')
            os.system('cls') 
        
        elif menu == 0:
            break