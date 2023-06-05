import os
listaNome=[]
listaDestino=[]
listaModelo=[]
nomeTripulacao=[]
while True:
    menu=input(' 1-Cadastro Cliente\n 2-Cadastro Passagem\n 3-Cadastro Avião\n 4-Cadastro Tripulação\n 5-imprimir a lista\n 6- Digite aqui:  ')

    if menu== '1':
        while True:
            try:
                print('===============Cadastro Cliente===============')
                nome=input('Digite seu nome: ')
                os.system('pause')
                os.system('cls')
                sobrenome=input('Digite seu sobrenome: ')
                os.system('pause')
                os.system('cls')
                rg=int(input('Digite seu rg: '))
                os.system('pause')
                os.system('cls')
                cpf=int(input('Digite seu cpf: '))
                os.system('pause')
                os.system('cls')
                endereco=input('Digite seu endereço: ')
                os.system('pause')
                os.system('cls')
                telefone=int(input('Digite seu telefone: '))
                os.system('pause')
                os.system('cls')
                idade=int(input('Digite sua idade: '))
                os.system('pause')
                os.system('cls')
            except ValueError:
                print('Digite apenas numeros!, sem ponto,traço,virgula, etc')
                continue
            else:
                listaNome.append(nome,sobrenome,rg,cpf,endereco,telefone,idade)
                break


    if menu=='2':
        while True:
            try:
                print('===============Cadastro Passagem==============') 
                destino=input('Digite seu destino: ')
                os.system('pause')
                os.system('cls')
                origem=input('Digite sua origem: ')
                os.system('pause')
                os.system('cls')
                duração=input('Digite sua duração da viagem: ')
                os.system('pause')
                os.system('cls')
                valordaPassagem=float(input('Digite o Valor da Passagem: '))
                os.system('pause')
                os.system('cls')
                desconto=0.05
                os.system('pause')
                os.system('cls')
            except ValueError:
                print('Digite apenas numeros!')
                continue
            else:
                listaDestino.append(destino,origem,duração,valordaPassagem,desconto)
                break
    if menu=='3':
        while True:
            try:
                print('===============Cadastro Avião=============')
                modelo=input('Digite o modelo de avião: ')
                os.system('pause')
                os.system('cls')
                ano=int(input('Digite o ano do avião: '))
                os.system('pause')
                os.system('cls')
                horaDeVoo=input('Digite a hora do voo: ')
                os.system('pause')
                os.system('cls')
                cor=input('Difite a cor do avião: ')
                os.system('pause')
                os.system('cls')
                quantidadeDePassageiro=int(input('Digite a quantidade de passageiro: '))
                os.system('pause')
                os.system('cls')
            except ValueError:
                print('Digite apenas numeros!')
                continue
            else:
                listaModelo.append(modelo,ano,horaDeVoo,cor,quantidadeDePassageiro)
                break
    if menu=='4':
        while True:
            try:
                print('===============Cadastro Tripulação==============')
                nome=input('Digite o nome da tripulação: ')
                os.system('pause')
                os.system('cls')
                descricao=input('Digite a descrição do cargo: ')
                os.system('pause')
                os.system('cls')
                idade=int(input('Digite a sua idade: '))
                os.system('pause')
                os.system('cls')
                dataDeAdimissao=input('Digite a data de adimissao: ')
                os.system('pause')
                os.system('cls')
                telefone=int(input('Digite seu telefone: '))
                os.system('pause')
                os.system('cls')
            except ValueError:
                print('Digite apenas numeros!, sem ponto,traço,virgula, etc')
                continue
            else:
                nomeTripulacao.append(nome,descricao,idade,dataDeAdimissao,telefone)
                break
    if menu== '5':
         while True:
            print('===============Cadastro Cliente===============')
            print(listaNome)
            print('===============Cadastro Passagem==============') 
            print(listaDestino)
            print('===============Cadastro Avião=============')
            print(listaModelo)
            print('===============Cadastro Tripulação==============')
            print(nomeTripulacao)
            os.system('pause')
        
    






