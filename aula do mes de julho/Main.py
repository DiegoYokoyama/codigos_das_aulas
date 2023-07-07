from Vendedor import *
'''vendedor1=Vendedor('Diego',1000)
print(vendedor1.nome,vendedor1.vendas)'''


nome=input('Digite um nome: ')
venda=float(input('Digite um valor: '))
vendedor1=Vendedor(nome,venda)
print(vendedor1.nome)
print(vendedor1.vendas) 
vendedor1=Vendedor(nome,venda)
vendedor1.bateu_meta(100)