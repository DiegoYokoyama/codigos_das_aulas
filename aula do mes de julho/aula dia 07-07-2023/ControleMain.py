import os
from Controle import *


while True:
    try:
        print('escolha alguma das opçoes\n1-Ligar a TV\n2-Desligar a TV\n3-Aumentar o volume\n4-Diminuir o volume\n5-Mudar de canal\n0-sair')
        escolha = int(input('Digite: '))
        escolha2 = Controle(escolha)
        if escolha == 1:
            escolha2.funcao_ligar()
        elif escolha == 2:
            escolha2.funcao_desligar()
        elif escolha == 3:
            escolha2.funcao_aumentar()
        elif escolha == 4:
            escolha2.funcao_diminuir()
        elif escolha == 5:
            escolha2.funcao_mudar()
        elif escolha == 0:
            break
        os.system("Pause")
        os.system("cls")
    except ValueError:
        print('digite um valor valido')
