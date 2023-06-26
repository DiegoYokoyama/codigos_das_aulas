def quantidade(a):
    nume=str(a)
    print(len(nume))
while True:
    try:
        num =input("Digite um número: ")
        quantidade(num)
    except ValueError:
        print('DIGITE APENAS NUMEROS INTEIRO É NÃO DIGITE LETRAS')
