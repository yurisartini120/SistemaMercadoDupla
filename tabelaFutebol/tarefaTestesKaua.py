import mysql.connector as mysql
from tabulate import tabulate
import random


times = []

class time:
        def __init__(self, nome): 
            self.nome = nome
            
class TabelaCampeonato:
    
    def criarTabela():
        cursor.execute("Create table if not exists  `teste2` (`id` int not null auto_increment primary key,`nome` varchar(255) not null, `partidas` int, `V` int, `D` int, `E` int, `SG` int, `pontos` int);")
        
    def adicionarTime():
        contador = 0
        contadorLimite = int(input("Digite quantos times você deseja adicionar: "))
        while (contador < contadorLimite):
            timeNome = input(f"Digite o nome do {contador+1}° time: ").lower()
            cursor.execute("insert into teste2 (nome, partidas, V, D, E, SG, pontos) VALUES (%s, %s, %s, %s, %s, %s, %s);", (timeNome , 0, 0, 0, 0, 0, 0))
            times.append(timeNome) 
            conexao.commit()
            
            contador+=1
        return times
    
    def visualizarTabela():  
    

        selecionarNomes = "Select `nome` From teste2"
        cursor.execute(selecionarNomes)
        resultadoNomes = cursor.fetchall()


        selecionarPartidas = "Select `partidas` From teste2"
        cursor.execute(selecionarPartidas)
        resultadoPartidas = cursor.fetchall()

        selecionarVitorias = "Select `V` From teste2"
        cursor.execute(selecionarVitorias)
        resultadoVitorias = cursor.fetchall()

        selecionarDerrotas = "Select `D` From teste2"
        cursor.execute(selecionarDerrotas)
        resultadoDerrotas = cursor.fetchall()

        selecionarEmpates = "Select `E` From teste2"
        cursor.execute(selecionarEmpates)
        resultadoEmpates = cursor.fetchall()

        selecionarSaldoDeGols = "Select `SG` From teste2"
        cursor.execute(selecionarSaldoDeGols)
        resultadoSaldoDeGols = cursor.fetchall()

        selecionarPontos = "Select `pontos` From teste2"
        cursor.execute(selecionarPontos)
        resultadoPontos = cursor.fetchall()

        nomes = [str(resultado[0]) for resultado in resultadoNomes]
        partidas = [str(resultado[0]) for resultado in resultadoPartidas]
        vitorias = [str(resultado[0]) for resultado in resultadoVitorias]
        derrotas = [str(resultado[0]) for resultado in resultadoDerrotas]
        empates = [str(resultado[0]) for resultado in resultadoEmpates]
        saldoDeGols = [str(resultado[0]) for resultado in resultadoSaldoDeGols]
        pontos = [str(resultado[0]) for resultado in resultadoPontos]


        dados_tuplas = list(zip(nomes, partidas, vitorias, derrotas, empates, saldoDeGols, pontos))
        dados = [list(tupla) for tupla in dados_tuplas]


        dados.insert(0, ["Nome", "Partidas", "V", "D", "E", "SG", "Pontos"])

        tabela = tabulate(dados, headers="firstrow", tablefmt="grid")
        print(tabela)
        conexao.commit()
    def executarJogo():
        valores = [0, 1, 2, 3, 4, 5, 6]
        time1 = input("Digite o nome do time 1: ").lower()
        time2 = input("Digite o nome do time 2: ").lower()
        
        if (time1 and time2 in times):
            golstime1= random.choice(valores)
            golstime2= random.choice(valores)
            mensagemResultado = (f"O resultado foi: \n {time1} {golstime1} X {golstime2} {time2}")
            
            if (golstime1 > golstime2):
                diferenca = golstime1-golstime2
                cursor.execute(f"update teste2 set pontos = pontos+3 where `nome` = '{time1}' ")
                cursor.execute(f"update teste2 set SG = SG+{diferenca} where `nome` = '{time1}' ")
                conexao.commit()
                print(mensagemResultado)
                
            elif (golstime1 < golstime2):
                diferenca = golstime1-golstime2
                cursor.execute(f"update teste2 set pontos = pontos+3 where `nome` = '{time2}'")
                cursor.execute(f"update teste2 set SG = SG+{diferenca} where `nome` = '{time2}'")
                conexao.commit()
                print(mensagemResultado)
                
                
            elif (golstime1 == golstime2):
                print(mensagemResultado)
                print("EMPATE!")
                
        else:
            print("Os times não estão na tabela!")
            


        
        

    

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

TabelaCampeonato.adicionarTime()

TabelaCampeonato.executarJogo()

TabelaCampeonato.visualizarTabela()





