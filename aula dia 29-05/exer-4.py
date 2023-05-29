numeros=[]
positivo=0
negativo=0
for a in range(10):
    numeros.append(int(input('Digite alguns numeros: ')))
for num in numeros:
    if num > 0:
        positivo += num
    elif num <0:
        negativo += num
print('O numero positivos:%d'%(positivo))
print("o numero negativos:%d"%(negativo))
