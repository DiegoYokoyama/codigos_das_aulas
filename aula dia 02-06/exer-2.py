maiorTemp=-1
menorTemp=9999999999999
temp=0
menor=0
maior=0
tempo=[]
while temp !='x':
    temp=input('Digite a temperatura: ')
    if temp=='x':
        print('fim')
        break
    temp=float(temp)
    mes=int(input('Digite o mes de 1 a 12: '))
    ano=int(input('Digite o ano: '))
    temp=int(temp)
    tempo.append(temp)
    if temp<menorTemp:
        menorTemp=temp
        menorMes=mes
        menorAno=ano
    
    if temp>maiorTemp:
        maiorTemp=temp
        maiorMes=mes
        maiorAno=ano
media=sum(tempo)/len(tempo)
print('a maior temperatura é:%.2f\n o ano que ocorreu essa temperatura:%d\n o mes que ocorreu essa temperatura:%d'%(maiorTemp,maiorAno,maiorMes))
print('a menor temperatura é:%.2f\n o ano que ocorreu essa temperatura:%d\n o mes que ocorreu essa temperatura:%d'%(menorTemp,menorAno,menorMes))
print('a media das temperatura é',media)


   
        



    

