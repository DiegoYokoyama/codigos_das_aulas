import os
n=[]
sobre=[]
srua=[]
bairo=[]
cid=[]
esta=[]      
paiis=[]
fone=[]
cpff=[]
pesso=[]
alt=[]
ida=[]
cartao=[]
cepp=[]
emai=[]
m1=[]
m2=[]
m3=[]
m4=[]
med=[]
seri=[]
clase=[]
sexoo=[]
corr=[]
cont=0
matricula=[] 
while True:
    op=input('1 - cadastro\n2 - consulta\n0 - sair\nDigite aqui: ')
    if op== '0':
        break
    elif op=='1':
        nome=input('Digite seu nome: ')
        n.append(nome)

        sobrenome=input('Digite seu Sobrenome: ')
        sobre.append(sobrenome)

        rua=input('Digite seu endereço sua rua e o numero da casa: ')
        srua.append(rua)

        bairro=input('Digite seu bairro: ')
        bairo.append(bairro)

        cidade=input('Digite sua cidade: ')
        cid.append(cidade)

        estado=input('Digite seu estado: ')
        esta.append(estado)

        pais=input('Digite seu pais: ')
        paiis.append(pais)

        telefone=float(input('Digite seu telefone: '))
        fone.append(telefone)

        cpf=float(input('Digite seu cpf: '))
        cpff.append(cpf)

        peso=float(input('Digite seu peso: '))
        pesso.append(peso)

        altura=float(input('Digite sua altura: '))
        alt.append(altura)

        idade=int(input('Digite sua idade: '))
        ida.append(idade)

        num_cartao=float(input('Numero do cartão: '))
        cartao.append(num_cartao)

        email=input('Digite seu email: ')
        emai.append(email)

        cep=float(input("Digite seu cep: "))
        cepp.append(cep)

        n1=float(input('Digite sua n1: '))
        m1.append(n1)
        n2=float(input('Digite sua n2: '))
        m2.append(n2)
        n3=float(input('Digite sua n3: '))
        m3.append(n3)
        n4=float(input('Digite sua n4: '))
        m4.append(n4)
        media=(n1+n2+n3+n4)/4
        med.append(media)

        serie=input('Digite sua serie: ')
        seri.append(serie)

        classe=input('Digite sua classe se e A,B,C: ')
        clase.append(classe)

        sexo=input('Digite seu sexo: ')
        sexoo.append(sexo)

        cor=input('Digite seu cor: ')
        corr.append(cor)

        cont=cont+1
        matricula.append(cont)
        os.system('pause')
    elif op=='2':
        mat=int(input('Digite a matricula : '))
        print(matricula[mat-1],'\n', n[mat-1],'\n', sobre[mat-1],'\n', srua[mat-1],'\n', bairo[mat-1],'\n', cid[mat-1],'\n', esta[mat-1],'\n', paiis[mat-1],'\n', fone[mat-1],'\n', cpff[mat-1],'\n', pesso[mat-1],'\n', alt[mat-1],'\n', ida[mat-1],'\n', cartao[mat-1],'\n', cepp[mat-1],'\n', emai[mat-1],'\n', m1[mat-1],'\n', m2[mat-1],'\n', m3[mat-1],'\n', m4[mat-1],'\n', med[mat-1],'\n', seri[mat-1],'\n', clase[mat-1],'\n', sexoo[mat-1],'\n', corr[mat-1])
        os.system('pause')




