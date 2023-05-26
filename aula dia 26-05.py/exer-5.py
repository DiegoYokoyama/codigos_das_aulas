idad=[]
while True:
    idade=int(input('Digite a idade ou 0 para sair: '))
    idad.append(idade)
    media=(sum(idad))/(len(idad))
    if idade == 0:
        print('sair')
        break
    elif media <=0 and media <=25:
        print('A media das idade é: %d'%(media))
    elif media <=26 and media<=60:
        print('A media das idade é: %d'%(media))
    else:
        print('A media das idade e: %d'%(media))     
        
        



