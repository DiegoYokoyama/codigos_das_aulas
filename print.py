import re

pattern=r=(input("digite algo: "))
string=(input('digite algo que tem aver com a primeira: '))
match=re.search(pattern,string)
if match:
    print('correspondencia encontrada',match.group())
else:
    print('nenhuma correspondencia encontrada')