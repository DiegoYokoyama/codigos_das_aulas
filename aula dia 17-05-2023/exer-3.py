n1=float(input('Digite sua nota 1: '))
n2=float(input('Digite sua nota 2: '))
media=(n1+n2)/2
if media>=7:
    print('Aprovado')
if media==10:
    print('Distinção')
elif media<7:
    print('Reprovado')
