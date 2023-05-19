salario=float(input('Coloque o seu salario: '))

if salario<500:
    salario_abaixo = salario  *0.15
    total=salario+salario_abaixo
    print('O salario anterior é: %.2f é o salario com o reajust : %.2f'%(salario,total))
elif salario>=500 and salario<=1000:
    salario_500_a_1000 = salario * 0.1
    total=salario+salario_500_a_1000
    print('O salario anterior é: %.2f é o salario com o reajust : %.2f'%(salario,total))
else:
    salario_acima = salario  *0.05
    total=salario+salario_acima
    print('O salario anterior é: %.2f é o salario com o reajust : %.2f'%(salario,total))

