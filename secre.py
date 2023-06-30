import secrets
import os
a='a'
sorte=[]
while a!='0':
    a=input('digite algo para colocar no sorteio: ')
    sorte.append(a)
    os.system('cls')
sorte.pop(-1)
print(sorte)
os.system('pause')
os.system("cls")
print(secrets.choice(sorte))