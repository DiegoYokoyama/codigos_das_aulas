import os
def somaImposto(x,y):
    a=((x*y)/100)+y
    return a
while True:
    try:
        custo=float(input('Digite o preço do produto: '))
        os.system('pause')
        os.system('cls')
        taxaImposto=int(input('Digite a taxa de imposto: '))
        os.system('pause')
        os.system('cls')
        print(somaImposto(taxaImposto,custo))
    except ValueError:
        print('Digite apenas numeros, no custo você pode pode usar numero quebrado mais na taxa de imposto não')



