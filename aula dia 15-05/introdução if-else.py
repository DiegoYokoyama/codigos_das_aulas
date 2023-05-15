#exemplo if e else
'''idade=18
if idade<20:
    print('Você é Jovem!')
print('oi, Fora do if')'''

#exemplo

idade=int(input('Escreva sua idade: '))
if idade==16: #caso for verdade
    print('pode votar')
else:
    if idade>16:
        print ('Pode dirigir')
    else:
        if idade < 16:
            print('Apenas estude')

