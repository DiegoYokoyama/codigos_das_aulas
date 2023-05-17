letra=input('Digite uma letra :')
num=letra.isdigit()
if num==True:
    print('você digitou um numero')
else:
    letra=letra.lower()
    if letra == float:
        print('Não permitido')  
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        print('A letra que você digitou e uma vogal: %s'%(letra))
    else:
        print('A letra que você digitou e uma consoante: %s'%(letra))

   
     
   
        
    


