def converter_24_para_12(hora,min):
    if hora<=12 and hora>=0:
        print(hora,':',min,'AM')
    elif hora>=12 and hora<=24:
        print(hora-12,':',min,'PM')
    else:
        print('Valor invalido')
while True:
    try:
        a=int(input('Digite um horario: '))
        b=int(input('Digite os minutos: '))
        print(converter_24_para_12(a,b))
    except ValueError:
        print('Digite apenas numeros validos sem letras')