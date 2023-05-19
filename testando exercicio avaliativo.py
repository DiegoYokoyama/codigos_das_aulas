#Atividade avaliativa para saber se o numero e divisível por 4, mas não por 6
print('================================================================================')
print('=                                  Bem Vindo                                   =') #coloquei um print com bem vindo
print('================================================================================')

num=int(input(' Por favor Digite um numero para ver se e  divisível por 4, mas não por 6: '))#esse e o comando para vc digitar um numero 
print('\n Você pode ver o resultado aqui em baixo !')                                     #coloquei esse printe para informar que o resultado vai sair em baixo dessa mensagem
if num % 4 == 0 and num % 6 != 0:                                                         #esse if e para saber se o numero digitado e divisível por 4, mas não por 6
    print('\n O numero e divisível por 4, mas não por 6: %d'%(num))                       #esse print vai falar se ele e divisível por 4,  mas não por 6 (coloquei o %d para mostrar o numero que eu digitei)
else:                                                                                     #esse else vai colocar o numero que e divisível por 6
    print('\n o numero não atende ao criterio: %d'%(num))                                 #esse print vai falar se ele divisível 4 e por 6 se for ele vai aparecer aqui 
print('================================================================================')
print('=                              Obrigado Volte Sempre                           =') #coloquei um print com obrigado Volte Sempre
print('================================================================================')

#para um numero ser divisível por 4 se os 2 ultimo numero e divisível por 4 exemplo 512,100,236
#agora alguns num que nao atende a esse criterio exemplo: 103,550,361
#fiquei um pouco bugado nesse exercicio mais acho que e isso 
#Um número é divisível por 6 se for par e a soma de seus algarismos for divisível por 3.