nomes=['Diego','Toshio','Yokoyama']
for n in nomes:
    print(n)
aluno='joao'
for a in aluno:
    print(a)
nomes=['Diego', 'Toshio','Yokoyama']
for n in nomes:
    print (n)
    if n == 'Toshio':
        break
nomes=['Diego','Toshio','Yokoyama']
for n in nomes:
    if n =='Toshio':
        continue
    print(n)
for x in range(100+1):
    print(x)

for x in range(2,6):#inicio/fim
    print(x)

for x in range(2,10,2):#inicio/fim/incremento ele vai pular de 2 em 2
    print(x)

for x in range(100,0,-1):#vai em ordem decrescente
    print(x)
    
for i in range(5):
    for j in range(6):
        print(i,j)