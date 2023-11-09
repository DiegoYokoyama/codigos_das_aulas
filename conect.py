import mysql.connector

con=mysql.connector.connect(
host = '10.28.1.138',
database = 'mercadinho',
user = 'suporte',
password = 'suporte')



if con.is_connected():
    mercadinho = con.get_server_info()
    print ("conecte ao banco = ", mercadinho)

    
    

    
    
    
comando = "insert into intensvenda(produto, quantidade) values ('bac', 005);"
cursor=con.cursor()
cursor.execute(comando)
con.commit


consulta_sql = 'select * from intensvenda '
cursor = con.cursor()
cursor.execute(consulta_sql)
linhas = cursor.fetchall()
print("NUMERO TOTAL DE REGISTRO" , cursor.rowcount)








    


print ("mostrando os  registros")
for linha in linhas:
    print("produto =", linha [1])
    print("quantidade = ", linha[2])
    
    
    
comando = ("update pessoa set nome 'Edsonr' where cpf = 12323231;")
cursor.execute(comando)
con.commit


comando = ("delete from pessoa where cpf = 12323231;")

    
"""consulta_sql = 'select * from produto '
cursor = con.cursor()
cursor.execute(consulta_sql)
linhas = cursor.fetchall()
print("NUMERO TOTAL DE REGISTRO" , cursor.rowcount)
    


print ("mostrando os  registros")
for linha in linhas:
    print("arroz =", linha [0])
    print("farinha = ", linha[1])"""