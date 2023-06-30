import enum
class animal(enum.Enum):
    cachorro=1
    gato=2
    pantera=2
if animal.cachorro is animal.gato:
    print('cao e gato sao os mesmo animais')
else:
    print('cao e gato sao animais diferentes')
if animal.pantera!= animal.gato:
    print('leao e gatos sao diferente')
else:
    print('pantera e gatos sao iguais')
    