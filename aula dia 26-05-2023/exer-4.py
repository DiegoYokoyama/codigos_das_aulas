nu=[]
while True:
    num=input("Digite um numero: ")
    
    if num == 'x':
        print("Encerrando")
        break
    num=int(num)
    nu.append(num)
print('os numeros menores somados são: ',min(nu))
print('os maiores numeros somados são: ',max(nu))
print('a soma dos numeros: ',sum(nu))




    