import os
def valorPagamento(prestacao,dias):
    jurosDias=(0.1*dias)/100
    multa=(prestacao*0.03)
    total=((prestacao*jurosDias)+multa)+prestacao
    return total

prestaca=[]
jurosdia=[]
mult=[]

while True:
    try:
        a=float(input('Digite o valor a pagar por uma prestação: '))
        b=float(input('digite os dias de atraso para ver os jutos: '))
        os.system("pause")
        os.system("cls")
    except ValueError:
        print('Digite apenas numeros')

    else:
        if a==0:
           os.system("cls")
           break
        elif a>0 and b>=0:
            prestaca.append(a)
            jurosdia.append(b)
            c=valorPagamento(a,b)
            mult.append(c)
            continue
        else:
            print('numero negativo por favor digite novamente')

print("------------------------------------------------------------------------------ Relatório do Dia ---------------------------------------------------------------------")
for a in prestaca:
    print('\nValores das Prestações em Ordem')
    print('R${:.2f}'.format(a))

for b in jurosdia:
    print('\nDias de Atraso em Ordem')
    print(b)

for c in mult:
    print('\nValores finais a serem pagados em ordem')
    print('R${:.2f}'.format(c))