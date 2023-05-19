num=int(input('Digite um numero inteiro: '))
if num>=1:
    print('O numero e positivo: %d'%(num))
else:  
    if num<0:
        print('O numero e negativo: %d'%(num))
    else:
        if num==0:
            print('O numero e neutro: %d'%(num))    

#outro meio que da pra fazer 

num=int(input('Digite um numero inteiro: '))
if num>0:
    print('O numero e positivo: %d'%(num))
elif num==0:
    print('O numero e neutro: %d'%(num))
else:
    print('O numero e negativo: %d'(num))