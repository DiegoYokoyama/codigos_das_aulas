maiorTemperatura = -1
menorTemperatura = 9999
temperatura = 0
menorMes = 0
menorAno = 0
maiorMes = 0
maiorAno = 0
temp = []
while temperatura != 'x' :
    temperatura = input("Digite a temperatura ou digite x para encerrar ")
    if temperatura == 'x':
        print("Fim!")
        break
    mes = input("Digite o Mês ")
    mes = int(mes)
    ano = input("Digite o ano ")
    ano = int(ano)
    temperatura = int(temperatura)
    temp.append(temperatura)
    if temperatura < menorTemperatura :
        menorTemperatura = temperatura
        menorMes = mes
        menorAno = ano
    if temperatura > maiorTemperatura :
        maiorTemperatura = temperatura
        maiorMes = mes
        maiorAno = ano
media = sum(temp)/len(temp)
print("A maior temperatura registrada foi %d,O ano que esta ocorreu foi em %d,no mês de %d"%(maiorTemperatura,maiorAno,maiorMes))
print("A menor temperatura registrada foi %d,O ano que esta ocorreu foi em %d,no mês de %d"%(menorTemperatura,menorAno,menorMes))
print("A media das temperaturas foi = ",media)
   