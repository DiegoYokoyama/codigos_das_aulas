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
print('Valores das Prestações em Ordem R$\n',prestaca)
print('Dias de Atraso em Ordem R$\n',jurosdia)
print('Valores finais a serem pagados em ordem R$\n',mult)    