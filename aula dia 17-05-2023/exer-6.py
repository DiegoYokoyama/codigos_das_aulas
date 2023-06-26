nome=input('qual e o nome do 1 produto: ')
preco=float(input('qual e o preço do 1 produto: '))

nome2=input('qual e o nome do 2 produto: ')
preco2=float(input('qual e o preço do 2 produto: '))

nome3=input('qual e o nome do 3 produto: ')
preco3=float(input('qual e o preço do 3 produto: '))

if preco<preco2 and preco<preco3: #preço 1 e mais barato
    print('o 1 produto e mais barato: %s\n o proço do produto: %.2f'%(nome,preco))
elif preco<preco3 and preco2<preco: #preço 2 e mais barato
    print('o 2 produto e mais barato: %s\n o preço do produto: %.2f'%(nome2,preco2))
else: #preço 3 e mais barato
    print('o 3 produto e mais barato: %s\n o preço do produto: %.2f'%(nome3,preco3))

