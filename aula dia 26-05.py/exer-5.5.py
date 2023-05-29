young=[]
adult=[]
old=[]
cont=0
ycont=0
acont=0
ocont=0 
test=False #Contadores, listas vazias, variável de teste.
while True:
    age=(input("Digite sua idade: ")) #Lê a idade.
    if age=="x":
        if test==True: #Caso ele tenha digitado algum número na idade anteriormente de apertar x.
            result2=(sum(young)+sum(adult)+sum(old))/cont
            if result2>=0 and result2<=25: #Caso a média da idade seja entre 0 e 25 anos.
                print("Pessoas entre 0 e 25 anos: {:d}\nPessoas entre 26 e 60 anos: {:d}\nPessoas com mais de 60 anos: {:d}\nResultado total de pessoas: {:d}\nMédia de idade da Turma: {:.0f}\nA sala é Jovem.".format(ycont,acont,ocont,cont,result2))
                break
            elif result2>25 and result2<=60: #Caso a média da idade seja entre 26 e 60 anos.
                print("Pessoas entre 0 e 25 anos: {:d}\nPessoas entre 26 e 60 anos: {:d}\nPessoas com mais de 60 anos: {:d}\nResultado total de pessoas: {:d}\nMédia de idade da Turma: {:.0f}\nA sala é Adulta.".format(ycont,acont,ocont,cont,result2))
                break
            elif result2>60: #Caso a média da idade seja maior que 60.
                print("Pessoas entre 0 e 25 anos: {:d}\nPessoas entre 26 e 60 anos: {:d}\nPessoas com mais de 60 anos: {:d}\nResultado total de pessoas: {:d}\nMédia de idade da Turma: {:.0f}\nA sala é Idosa.".format(ycont,acont,ocont,cont,result2))
                break
        elif test==False: #Caso so aperte x de primeira.
            print("Você não digitou nenhuma idade.")
            break
    age=int(age) #Converte a variável idade para inteiro.
    test=True #Converte o teste para válido.
    cont=cont+1 #Contador para usar como dividendo.
    if age>=0 and age<=25: #Caso a idade digitada seja entre 0 e 25 anos.
        ycont=ycont+1
        young.append(age)
    elif age>25 and age<=60: #Caso a idade digitada seja entre 26 e 60 anos.
        acont=acont+1
        adult.append(age)
    elif age>60: #Caso a idade digitada seja maior que 60.
        ocont=ocont+1
        old.append(age)