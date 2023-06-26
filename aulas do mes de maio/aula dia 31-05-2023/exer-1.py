cont1=0
cont2=0
cont3=0
total=0
eleitor=int(input('Digite a quantidade de eleitores: '))
for a in range(eleitor):
    tabela=int(input('Digite\n 1-para marcos\n 2-para felipe\n 3-para fernando\nescolha um numero:'))
    if tabela == 1:
        cont1 +=1
    elif tabela == 2:
        cont2+=1
    elif tabela == 3:
        cont3+=1
    total=total+1
print('o numero de votos do candidato marcos: %d'%(cont1))
print('o numero de votos do candidato felipe: %d'%(cont2))
print('o numero de votos do candidato fernando: %d'%(cont3))
print('numeros total de candidatos que votou: ',total)
