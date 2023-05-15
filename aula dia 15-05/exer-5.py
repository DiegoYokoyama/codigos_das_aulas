n1=float(input('Digite sua nota 1: '))
n2=float(input('Digite dua nota 2: '))
med=(n1+n2)/2
if med>=7:
    print('Aprovado')
elif med>=5 and med<=6.99:
    print('Recuperação')
else:
    print('Reprovado')

