turno=input('que turno vc estuda M=matutino V=vespertino N=noturno: ')
turno=turno.upper()
if turno=='M':
    print('Bom dia')
elif turno=='V':
    print('Boa tarde')
else:
    print('Boa noite')