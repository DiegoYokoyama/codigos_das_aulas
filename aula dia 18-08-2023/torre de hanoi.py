while True: 
    def torre_hanoi(x,origem, destino, auxiliar):
        if x == 1:
            print(f'mova o disco 1 de {origem} para {destino}')
            return 1
        movimentos = 0
        movimentos += torre_hanoi(x - 1, origem, auxiliar, destino)
        print(f'mova o disco {x} de {origem} para {destino}')
        movimentos +=1
        movimentos += torre_hanoi(x - 1, auxiliar, destino, origem)
        return movimentos
    try:
        num_discos = (int(input('Digite um numero de disco: ')))
        total_movimento = torre_hanoi(num_discos, 'A', 'B' , 'C')
        print (f'Total de movimento necessarios: {total_movimento}')
    except ValueError:
        print('Digite apenas numeros')
        
    