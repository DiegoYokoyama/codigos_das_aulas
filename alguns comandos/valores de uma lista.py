a=[10,20,30,40,50,60,70,80,90]
print(a)
print(type(a))
b=('pythos',3.5,'true',1)
print(b)
print(type(b))

-------------------------------------------------------------------------
a=['oi',1,2.5,[5,6]]
print(len(a))
print(type(a))

----------------------------------------------------------------------
#vai imprimir o elemento (h do cachorro)

a=[3,67,'gato',[56,57,'cachorro'],[],3.14,False]
print(a[3][2][3])

---------------------------------------------------------------------------------
#(in) serve para ver se tem essa palavra na list é (not in) serve para ver se aquela palavra nao esta na lista

animais=['gato','cachorro']
print('gato'in animais)
print('arara'not in animais)

-----------------------------------------------------------------------------------
#vai imprimir os elementos

a=[1,2,3,4,5,6,7,8,9]
print(a)
print(max(a))
print(min(a))
print(sum(a))
print(sum(a)/len(a))

-------------------------------------------------------------------------------------
#vai selecionar oque vc ta marcando 

list=['a','b','c','d','e','f']
print(list[1:3])
print(list[:4])
print(list[3:])
print(list[:])
print(list[0:6])

------------------------------------------------------------------------------------------
#list são mutações vc pode pudar 

frutas=['banana','maça','cereja']
frutas[0]='pera'
frutas[-1]='laranja'
print(frutas)

itens=['bola','celular','tenis']
itens[0]='oculos'
itens[1]='teclado'
print(itens)

--------------------------------------------------------------------------------------------
#troca o elemento na lista

list=['flor','azul',[1,'casa']]
list[2][1]='escola'
print(list)

--------------------------------------------------------------------------------------------
#muda mais de um elemento na lista

list=['a','b','c','d','e','f']
list[1:3]=['x','y']
print(list)

------------------------------------------------------------------------------------------
#vai excluir o elemento que vc marcou

list=['a','b','c','d','e','f']
print(list)
print(len(list))

list[1:3]=[]
print(list)
print(len(list))

------------------------------------------------------------------------------------------
#pode inserir/adicionar um elemento em uma list

list=['a','d','f']
list[1:1]=['b','c']
print(list)
list[4:4]=['e']
print(list)
list[6:6]=['g','h','i']
print(list)

------------------------------------------------------------------------------------------
list=[4,2,8,6,5]
list[2]=[True]
print(list)

------------------------------------------------------------------------------------------
#vai deletar o elemento selecionado

a=['um','dois','tres']
del a[1]
print(a)

list=['a','b','c','d','e','f']
del list[1:5]
print(list)

------------------------------------------------------------------------------------------
#append adiciona o elemento no final da lista

a=[81,82,83]
a.append(55)
print(a)

------------------------------------------------------------------------------------------
#(sort) ordena em ordem crecente (reverse) ordena em decrecente

a=[2,7,1,6,2,5,87,3,65,32,4,7,34,]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

------------------------------------------------------------------------------------------
#index mostra qual a posição 

a=[1,2,3,4,5,6,7,8,9,0]
print(a.index(4))

------------------------------------------------------------------------------------------
#insert vai adicionar um elemento na lista

a=[88,81,82,83]
a.insert(2,100)
print(a)

------------------------------------------------------------------------------------------
#count mostra quantas vezes o elemento informado aparece na lista

a=[1,2,3,4,5,6,7,8,9,0]
print(a.count(4))

------------------------------------------------------------------------------------------
#pop remove o ultimo elemento da lista se nao selecionado / se vc selecionar vc remove oque vc selecionou 

a=[1,2,3,4,5,6,7,8]
a.pop()
print(a)
a.pop(4)
print(a)
