menor = 9999999999
maior=-1
somaA=0
somaA2000=0
cont=0
for a in range(1,6):
    veiculos=int(input('Digite um numero de veiculo de passeio: '))
    acidente=int(input('Digite o numero de acidente: '))
    if acidente<menor:
        menor=acidente
        cidadeMenor=a+1
    if acidente>maior:
        maior=acidente
        cidadeMaior=a+1
    somaA=somaA+acidente
    if veiculos <2000:
        somaA2000=somaA2000+acidente
        cont=cont+1
    media=somaA/5
    media2000=somaA2000/cont

print('o numero de veiculo menores',menor,'o numero de acidente menores',cidadeMenor)
print('o numero de veiculo maiores',maior,'o numero de acidente maiores',cidadeMaior)
print(somaA2000)
print(media)
print(media2000)
                

