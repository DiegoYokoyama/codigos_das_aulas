def hello():
    print('ola')
hello()
#===============================================
def hello(name):
    print('ola',name)
hello('Diego')    
#===============================================
def hello(name):
    name=input('Digite um nome: ')
    print(name)
hello('name')  
#===============================================
def hello(nome,idade):
    print('oi ',nome,'\nsua idade ',idade)
hello('Diego',19)
#===============================================
def calcular_pagamento(quant_hora,valor_hora):
    hora=float(quant_hora)
    taxa=float(valor_hora)
    if hora<=40:
        salario=hora*taxa
    else:
        hora_exe=hora-40
        salario=40*taxa+(hora_exe*(1.5*taxa))

        print(salario)
calcular_pagamento(50,20)
#===============================================
def soma(x,y):
    result=x+y
    return result
a=int(input('Digite um primeiro numero: '))
b=int(input('Digite um segundo numero: '))
res=soma(a,b)
print('soma:',res)
#===============================================
def inverte(nome,sobrenome):
    nomeInverso=sobrenome+','+nome
    return nomeInverso
nome=input('escreva seu Nome: ')
sobrenome=input("escreva seu Sobrenome: ")
invertido=inverte(nome,sobrenome)
print(invertido)
#===============================================
def cadastro():
    name=input('qual seu nome: ')
    age=int(input('Digite sua idade: '))
    return name,age
print('Iniciando cadastro')
nome,idade=cadastro()
print('cadastro realizado com sucesso: ')
print('Seu nome é',nome,'\nSua idade é',idade)
#===============================================
def par(x):
    if x%2==0:
        return True
    else:
        return False
while True:
    num=int(input('insira um numero: '))
    if par(num):
        print(num,'E par')
    else:
        print(num,'E impar')


