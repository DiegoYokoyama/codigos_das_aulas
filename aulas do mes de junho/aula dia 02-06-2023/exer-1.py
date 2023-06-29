cont1=0
cont2=0
for a in range(10):
    num=int(input('Digite ums numeros inteiro: '))
    if num % 2 ==0:
        cont1+=1
    else:
        cont2+=1
print('numero par: %d'%(cont1))
print('numero impar: %d'%(cont2))
