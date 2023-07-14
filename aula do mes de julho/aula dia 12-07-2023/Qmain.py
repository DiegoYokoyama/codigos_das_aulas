import os
from Quadrado import *


while True:

    try:
        menu=int(input("1-Tamanho do quadrado\n2-Mostrar area do quadrado\n3-Mudar o valor do lado do quadrado\n0-Sair\nDigite aqui: "))
        os.system('cls')

    except ValueError:
        os.system('cls')
        print('Digite apenas numeros inteiros')
        os.system('pause')
        os.system('cls')

    else:

        if menu ==1:
            try:
                LadoQuadrado = float(input('Digite um valor do lado do quadrado: '))
                os.system('pause')
                os.system('cls')

                lado = Quadrado(LadoQuadrado)
            except ValueError:
                print('Digite apenas numeros validos')
                os.system('pause')
                os.system('cls')

        elif menu ==2:
            lado.AreaQuadrado()
            os.system('pause')
            os.system('cls')


        elif menu ==3:
            try:
                MudarValor=float(input('Digite o valor que vc quer mudar: '))
                lado.MudarValorLado(MudarValor)
                os.system('pause')
                os.system('cls')

            except ValueError:
                print('Digite apenas numeros validos')
                os.system('pause')
                os.system('cls')

        elif menu ==0:
            break
