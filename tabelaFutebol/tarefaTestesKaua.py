import mysql.connector as mysql

#use para conectar (o banco de dados ja tem q estar criado)
database = "teste"


conexao = mysql.connect(
host ='127.0.0.1',
port=3306,
database = database,
user = 'root',
password=''
)

cursor = conexao.cursor()

cursor.execute("Create table if not exists  `teste` (`id` int not null auto_increment primary key,`nome` varchar(255) not null, `pontos` int);")



# class time:
#         def __init__(self, nome, quantidadePontos):
#             self.nome = nome
#             self.quantidadePontos = quantidadePontos

            


# nome = input("Nome do time:")
# quantidadePontos = int(input("Quantidade de pontos: "))

# flamengo = time(nome=nome, quantidadePontos=quantidadePontos)




