#input

print("digite seu nome")
nome=input()
print(nome)

#outro tipo e assim 

nome=input("digite seu nome: ")
print(nome)

#input idade
 
idade=input("Digite sua idade: ")
print(type(idade))

#input salario

salario=int(input('Salario?='))
imposto=float(input('Digite o imposto= '))

# 2 Tipos de concatenação

a=500
b=500.56
c='Diego'
print('o valor de a é %d: o valor de b é %.2f: o nome de c é: %s' % (a,b,c))
print('o valor de a é',a,'e o valor de b',b,'o nome de c é',c)
#string (s) é comentario ex: nome 
#inteiro (d) é numeros inteiro ex: 50, 100
#boleano (b) é e verdadeiro ou falso : True ou False
#fload (f) é real numeros ex 50.23 , 100,54 (vc coloca %.2f PODE SER QUANTOS NUMEROS VC QUISER POIS ELE VAI MOSTRAR QUANTAS CASA DECIMAIS VC VAI QUERER)
#porcentagem (%) é concatenação


#place rouder interpolação

nome=(input('nome='))
sal=float(input('Salario='))
print("o funcionario %s e o salario é %.2f" %(nome,sal))
 
 #concatenação outro exemplo, so funciona com string 

a='Diego'
b='Toshio'
print('prezado '+a+' '+b+'.'+' Ola!')

#replica de string

print(10*'Diego\n')

print("+"+10*"-"+"+")
print(("|"+" "*10+"|\n")*5,end="")
print("+"+10*"-"+"+")


