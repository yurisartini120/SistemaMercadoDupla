import mysql.connector as mysql

#use para conectar (o banco de dados ja tem q estar criado)
database = input("Digite um database que você deseja conectar: ")


conexao = mysql.connect(
host ='127.0.0.1',
port=3306,
database = database,
user = 'root',
password=''
)

class time:
        def __init__(self, nome, quantidadePontos):
            self.nome = nome
            self.quantidadePontos = quantidadePontos

            


nome = input("Nome do time:")
quantidadePontos = int(input("Quantidade de pontos: "))

flamengo = time(nome=nome, quantidadePontos=quantidadePontos)





