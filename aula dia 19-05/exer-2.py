import os
while True:
    print('*','='*70,'*')
    print('                           Bem Vindo a Calculadora                       \n')
    print(' 1=Multiplicação \n 2=Divisão \n 3=Adição \n 4=Subtração \n 5=Volume de um cubo \n 6=exponemciação \n 7=Raiz quadrada \n 8=Area de um quadrado \n 9=Media 4 numero \n 10=Fatoração \n 0=Sair')
    calculadora=int(input(' Digite o numero que vc vai querer usar: '))
    if calculadora == 1:
        n1=float(input('Digite um numero: '))
        n2=float(input('Digite outro numero: '))
        total=n1*n2
        print('A resultado é: %.2f'%(total))
        os.system('pause')

    elif calculadora == 2:
        n1=float(input('Digite um numero: '))
        n2=float(input('Digite outro numero: '))
        total=n1/n2
        print('A resultado é: %.2f'%(total))
        os.system('pause')

    elif calculadora == 3: 
        n1=float(input('Digite um numero: '))
        n2=float(input('Digite outro numero: '))
        total=n1+n2
        print('A resultado é: %.2f'%(total))
        os.system('pause')

    elif calculadora == 4:
        n1=float(input('Digite um numero: '))
        n2=float(input('Digite outro numero: '))
        total=n1-n2
        print('A resultado é: %.2f'%(total))
        os.system('pause')

    elif calculadora == 5:
        n1=float(input('Digite um numero: '))
        total=n1**3
        print('A resultado é: %.2f'%(total))
        os.system('pause')

    elif calculadora == 6:
        n1=float(input('Digite um numero: '))
        total=n1**n1
        print('A resultado é: %.2f'%(total))
        os.system('pause')

    elif calculadora == 7:
        n1=float(input('Digite um numero: '))
        total=(n1**(0.5))
        print('A resultado é: %.2f'%(total))
        os.system('pause')

    elif calculadora == 8:
        n1=float(input('Digite a altura de um quadrado: '))
        total=n1**2
        print('A resultado é: %.2f'%(total))
        os.system('pause')

    elif calculadora == 9:
        n1=float(input('Digite um numero: '))
        n2=float(input('Digite um segundo numero: '))
        n3=float(input('Digite um terceiro numero: '))
        n4=float(input('Digite um quarto numero: '))
        total=(n1+n2+n3+n4)/4
        print('A resultado é: %.2f'%(total))
        os.system('pause')

    elif calculadora == 10:
        num=float(input("Digite um número para ter seu fatorial: "))
        result=1
        cont=1
        while cont<=num:
            result*=cont
            cont+=1
        print("O resultado é %.2f"%(result))    
        os.system('pause')
    else:
        ('Sair')
        break

        