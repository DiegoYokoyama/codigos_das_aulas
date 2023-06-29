def argu(a):
    if a>0:
        result='p'
        return result
    elif a<=0:
        result='n'
        return result
while True:
    try:
        num=int(input('insira um numero: '))
        print(argu(num))
    except ValueError:
        print('Digite um valor sem ser quebrado é não digite uma letra')



    