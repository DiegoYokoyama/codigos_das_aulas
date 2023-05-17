num=int(input('Digite um numero: '))
num2=int(input('Digite outro numero: '))
num3=int(input('Digite outro numero: '))

if num>num2 and num2>num3:
    print(num,num2,num3)
elif num>num3 and num3>num2:
    print(num,num3,num2)

elif num2>num and num>num3:
    print(num2,num,num3)
elif num2>num3 and num3>num:
    print(num2,num3,num)

elif num3>num2 and num2>num:
    print(num3,num2,num)
elif num3>num and num>num2:
    print(num3,num,num2)


lista = [num,num2,num3]
lista.sort(reverse=True)
print(lista)
