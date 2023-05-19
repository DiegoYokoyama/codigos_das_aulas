#Atividade avaliativa para saber se o numero e divisível por 4, mas não por 6
print('===========================================================================')#coloquei um print com (=) so pra ficar bonito
print('                                Boa Tarde                                  ') #coloquei um print com Boa Tarde
print('===========================================================================')#coloquei um print com (=) so pra ficar bonito

num=int(input('Digite um numero para ver se e  divisível por 4, mas não por 6: '))#esse e o comando para vc digitar um numero 
if num % 4 == 0 and num % 6 != 0: #esse if e para saber se o numero digitado e divisível por 4, mas não por 6
    print('O numero e  divisível por 4 mas não por 6: %d'%(num))#esse print vai falar se ele e divisível por 4,  mas não por 6 (coloquei o %d para mostrar o numero que eu digitei)
else:#esse else vai colocar o numero que e divisível por 6
    print('o numero não atende ao criterio: %d'%(num))#esse print vai falar se ele divisível por 6 se for ele vai aparecer aqui 
print('Obrigado volte Sempre que tiver duvida')#coloquei um printe com obrigado 

#para um numero ser divisível por 4 se os 2 ultimo numero e divisível por 4 exemplo 512,100,236
#agora alguns num que nao atende a esse criterio exemplo: 103,550,360
#fiquei um pouco bugado nesse exercicio mais acho que e isso 