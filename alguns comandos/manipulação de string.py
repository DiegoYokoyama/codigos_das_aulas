#casefold e lower deixa todas as letras maiuscula em minuscula são os mesmo
a='DIEGO'
print(a.casefold())
print(a.lower())

#capitalize faz a primeira letra ficar em maiusculo  ex(diego) vai ficar Diego so o D vai ficar maiusculo
a="diego"
print(a.capitalize())

#find mostra a primeira aparição da palavra, letra onde começa na string
a="Diego Toshio Yokoyama"
print(a.find("Yokoyama"))

#função len serve para contar quantas caracter tem uma variavel ex (Diego) vai contar como 5 caracter
a="Diego Toshio"
print(len(a))# so serve para string(str)

#in ele vai procurar se tem a palavra 
a="Diego Toshio Yokoyama"
print("Yokoyama"in a)

#isdigit verifica se a string so possui numeros se tiver so numeros vai ver(True) se nao tiver so numeros vai ser (false)
a="123987"
print(a.isdigit())
a="16768abc"
print(a.isdigit())

#islower fala se a variavel e minusculo se for vai ser (True) se nao for vai ser (False) 
#isupper ve se a variavel e maiusculo se for vai ser (True) se nao for vai ser (False)
a="DIEGO"
print(a.islower())
print(a.isupper())

#Replase troca as string com oque vc quer trocar tipo (Diego Toshio) quero trocar o Toshio por (Yokoyama) ae vc coloca print(a.replace("Toshio","Yokoyama"))
a="Diego Toshio"
print(a.replace("Toshio","Yokoyama"))

#rfind conta da direita para esquerda
a="Diego Toshio Yokoyama "
print(a.rfind("Toshio"))

#count conta quantas vezes pareceu a palavra ex :a
a="Diego Toshio Yokoyama"
print(a.count("a"))

#split substitui o parametro por virgula ex:Diego-Toshio vai ficar ['Diego','Toshio']
a="Diego-Toshio-Yokoyama"
print(a.split("-"))

#upper transforma todas as letras em maiusculo
a="diego toshio"
print(a.upper())

#substring conta da esquerda para a direita que começa do 0 e fala qual e a letra que esta
s="Ola, mundo!"
print(s[0])
print(s[2])
print(s[6])
#substring conta da direita para a esquerda que começa do -1 e fala qual e a letra que esta
s="Ola, mundo!"
print(s[-11])
print(s[-9])
print(s[-5])

#slice ele corta a palavra no intervalo que vc celeciona pelo numero ex (S[1:3]) ele vai pegar so a letra que esta na 1 e 2 tipo Ola ia pegar so o la
s="Ola, mundo!"
print(s[1:3])
#se nao tiver mencionado o inicio ele vai ate onde vc colocou para terminar 
s="Ola, mundo!"
print(s[:3])
#o mesmo vale se vc mencionar o mumero inicial mais nao colocar um nujmero final
s="Ola, mundo!"
print(s[5:])