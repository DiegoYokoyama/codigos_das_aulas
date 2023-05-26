soma=[]
num=int(input('Digite um numero: '))
num2=int(input('Digite outro numero: '))
for a in range(num+1,num2):
    print('numero entre o numeros digitados',a)
    soma.append(a)
    print(sum(soma))
