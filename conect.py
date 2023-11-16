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
    
    
    
'''os.system('cls')
        sql_cadastro = (f'{nome},{cpf},{endereco},{sexo},{idade},{rg},{email},{cidade},{estadoCivil},{escolaridade}')
        cursor = con.cursor()
        cursor.execute(sql_cadastro)
        
        sql_select = 'select * from Usuario'
        cursor = con.cursor()
        cursor.execute(sql_select)   
        linhas = cursor.fetchall()'''
        
        
        
        
        
'''class BancoSQL:
    def __init__(self):
        self.UserCadastro = mysql.connector.connect ( 
        host = '10.28.1.135',
        database = 'UserCadastro',
        user = 'Toshio',
        password = 'DiegoToshio.2003'
        )
        if self.UserCadastro.is_connected():
            database_informacao = self.UserCadastro.get_server_info()
            print(f"Conectado ao Banco de Dados = {database_informacao}")
            
        self.cursor = self.UserCadastro.cursor()
        
        today = "insert into TelaDeCadastro (nome, cpf, endereco,sexo,idade,rg,email,cidade,estadoCivil,escolaridade) values (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s)"
        values = (nome, cpf, endereco,sexo,idade,rg,email,cidade,estadoCivil,escolaridade)

        self.cursor.execute(today, values)
        self.UserCadastro.commit()
        print(self.cursor.rowcount, "registro(s) inserido(s).")
        
    def fechar_conexao(self):
        if self.UserCadastro.is_connected():
            self.UserCadastro.close()
            print("Conexão encerrada")
            print("-=" * 20)'''