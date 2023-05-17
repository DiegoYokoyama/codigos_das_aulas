num=int(input('Digite um numero: '))
num2=int(input('Digite um segundo numero: '))
num3=int(input('Digite um terceiro numero: '))

if num>num2 and num>num3 : #o numero 1 e maior
    print('o numero 1 e maior: %d' %(num))
elif num2>num3 and num2>num: #o 2 produto e maior
    print('o numero 2 e maior: %d' %(num2))
else: #o 3 numero e maior
    print('o numero 3 e maior: %d' %(num3))