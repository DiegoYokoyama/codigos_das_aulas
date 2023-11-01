import mysql.connector



con = mysql.connector.connect(
host = "10.28.1.135",
database = "hub_innovation",
user = "Toshio",
password = "DiegoToshio.2003")

if con.is_connected():
    hub_innovation = con.get_server_info()
    print("conectado ao banco de dados =",hub_innovation)


    consulta_sql = "select *from palestras"
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()
    print("numero total de registros retornados:", cursor.rowcount)
    
    print('Mostrando os Registros')
    for linha in linhas:
        print("palestraID = ",linha[0])
        print("palestraTema= ", linha[1])
        
    if  con.is_connected():
     #cursor.close()
     con.close()
    print("conexao encerrada")