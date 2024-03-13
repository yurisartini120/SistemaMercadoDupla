import mysql.connector as mysql
import time 
import random


class time:
        def __init__(self, nome):
            self.nome = nome
            
class TabelaCampeonato:
    def criarTabela():
        cursor.execute("Create table if not exists  `teste2` (`id` int not null auto_increment primary key,`nome` varchar(255) not null, `partidas` int, `V` int, `D` int, `E` int, `SG` int, `pontos` int);")
        
    # def adicionarTime():
    #     contador = 0
    #     while contador != 8:
    #         timeNome = input("Digite o nome do time: ")
    #         cursor.execute("insert into teste2 (nome, partidas, V, D, E, SG, pontos) VALUES (%s, %s, %s, %s, %s, %s, %s);", (timeNome , 0, 0, 0, 0, 0, 0))
            
    #         contador+=1
    #         conexao.commit()


selecionar = "Select * From teste2"
          
            
# class jogo:
    
#     timeCasa = input("time da casa:")
#     cursor.execute()
#     timeDesafiante = input("time desafiante:")
#     pontos = 0
   
#     golsCasa = 0
#     golsDesafiante = 0

#     time.sleep(0.5)
#     print("------------------------------------------")
#     print(golsCasa, "X", golsDesafiante)
#     time.sleep(0.5)
    
#     if (golsCasa > golsDesafiante):
#         print(timeCasa, "Vencedor com ",golsCasa, "GOLS")
#         pontos += 3
#         print("pontuação: +", pontos)
        
#     elif(golsCasa == golsDesafiante):
#         print("Empate!")
#         pontos += 1
#         print("pontuação para ambos: +", pontos)
        
#     elif(golsDesafiante > golsCasa):
#         print(timeDesafiante, "Vencedor com ",golsDesafiante, "GOLS")
#         pontos += 3
#         print("pontuação: +", pontos)
#     print("------------------------------------------")
        
        

    
    
    

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


TabelaCampeonato.criarTabela()

# TabelaCampeonato.adicionarTime()

cursor.execute(selecionar)
resultado = cursor.fetchall()
print(resultado)
conexao.commit()







            


# nome = input("Nome do time:")
# quantidadePontos = int(input("Quantidade de pontos: "))

# flamengo = time(nome=nome, quantidadePontos=quantidadePontos)




