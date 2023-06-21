def converter_24_para_12(x,y):
    if x ==24 and y ==0:
        return "12:00 AM"
    elif x>=0 and x<= 11:
        return f"{x}:{y:02d} AM"
    elif x == 12:
        return f"{x}:{y:02d} PM"
    elif x >= 13 and x <= 23:
        return f"{x - 12}:{y:02d} PM"
while True:
    a=int(input('Digite um horario: '))
    b=int(input('Digite os minutos: '))
    print(converter_24_para_12(a,b))
