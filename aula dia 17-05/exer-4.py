num=int(input('Digite um numero: '))
num2=int(input('Digite um segundo numero: '))
num3=int(input('Digite um terceiro numero: '))

if num>num2>num3 :
    print('o numero 1 e maior: %d' %(num))
elif num2>num3>num:
    print('o numero 2 e maior: %d' %(num2))
else:
    print('o numero 3 e maior: %d' %(num3))