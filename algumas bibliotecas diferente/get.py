from getpass import getpass
senha=getpass("Digite: ")
confirmar_se=getpass('confirmar: ')
if senha==confirmar_se:
    print('senha correta')
else:
    print('senha incorreta')