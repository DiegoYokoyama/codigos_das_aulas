import re

pattern=r=(input("digite algo: "))
string=(input('digite algo que tem aver com a primeira: '))
match=re.search(pattern,string)
if match:
    print('correspondencia encontrada',match.group())
else:
    print('nenhuma correspondencia encontrada')

    #A re.search()função procura um padrão dentro de uma string e retorna um objeto de correspondência se uma correspondência for encontrada.
    #exemplo se na pattern tiver (oi ) e eu escrever na string(oi bem vindo) vai pegar so o (oi ) pq na pattern so tem o (oi)
    #outro exemplo se na pattern tiver (ola) e na string tiver so (oi) nao vai retornar nada pq nao tem nenhuma palavra igual