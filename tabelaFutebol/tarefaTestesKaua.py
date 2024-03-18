import mysql.connector as mysql
from tabulate import tabulate
import random




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
            conexao.commit()
            
            contador+=1

    def visualizarTabela():  
        
        
    

        selecionarNomes = "Select `nome` From teste2 order by `pontos` desc;" 
        cursor.execute(selecionarNomes)
        resultadoNomes = cursor.fetchall()


        selecionarPartidas = "Select `partidas` From teste2 order by `pontos` desc;"
        cursor.execute(selecionarPartidas)
        resultadoPartidas = cursor.fetchall()

        selecionarVitorias = "Select `V` From teste2 order by `pontos` desc;"
        cursor.execute(selecionarVitorias)
        resultadoVitorias = cursor.fetchall()

        selecionarDerrotas = "Select `D` From teste2 order by `pontos` desc;"
        cursor.execute(selecionarDerrotas)
        resultadoDerrotas = cursor.fetchall()

        selecionarEmpates = "Select `E` From teste2 order by `pontos` desc;"
        cursor.execute(selecionarEmpates)
        resultadoEmpates = cursor.fetchall()

        selecionarSaldoDeGols = "Select `SG` From teste2 order by `pontos` desc;"
        cursor.execute(selecionarSaldoDeGols)
        resultadoSaldoDeGols = cursor.fetchall()

        selecionarPontos = "Select `pontos` From teste2 order by `pontos` desc;"
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
        while True:
            time1 = input("Digite o nome do time 1: ").lower()
            time2 = input("Digite o nome do time 2: ").lower()

            cursor.execute("Select `nome`, `SG` from teste2")
            dadosTimes = cursor.fetchall()
            times = {row[0].lower(): row[1] for row in dadosTimes}

            if time1 in times and time2 in times:
                break
            else:
                print("Um ou ambos os times não estão cadastrados. Por favor, tente novamente.")

        golstime1 = random.choice(valores)
        golstime2 = random.choice(valores)
        mensagemResultado = (f"O resultado foi: \n {time1} {golstime1} X {golstime2} {time2}")

        if golstime1 > golstime2:
            diferencaPositivo = golstime1 - golstime2
            diferencaNegativo = golstime2 - golstime1
            

            cursor.execute(f"update teste2 set pontos = pontos+3, partidas = partidas+1, SG = SG+{diferencaPositivo}, V = V+1 where `nome` = '{time1}' ")
            
            
            cursor.execute(f"update teste2 set D = D+1, partidas = partidas+1 where `nome` = '{time2}' ")
            if times[time2] > 0:
                cursor.execute(f"update teste2 set SG = SG-{diferencaNegativo} where `nome` = '{time2}' ")
            
            conexao.commit()
            print(mensagemResultado)

        elif golstime1 < golstime2:
            diferencaPositivo = golstime2 - golstime1
            diferencaNegativo = golstime1 - golstime2
            
            # Atualizar as estatísticas para o time vencedor
            cursor.execute(f"update teste2 set partidas = partidas+1, pontos = pontos+3, SG = SG+{diferencaPositivo}, V = V+1 where `nome` = '{time2}' ")
            
            # Atualizar as estatísticas para o time perdedor
            cursor.execute(f"update teste2 set D = D+1, partidas = partidas+1 where `nome` = '{time1}' ")
            if times[time1] > 0:
                cursor.execute(f"update teste2 set SG = SG-{diferencaNegativo} where `nome` = '{time1}' ")
            
            conexao.commit()
            print(mensagemResultado)

        elif golstime1 == golstime2:
            print(mensagemResultado)
            # Atualizar as estatísticas para ambos os times em caso de empate
            cursor.execute(f"update teste2 set pontos = pontos+1, E = E+1, partidas = partidas+1 where `nome` = '{time1}' ")
            cursor.execute(f"update teste2 set pontos = pontos+1, E = E+1, partidas = partidas+1 where `nome` = '{time2}' ")
            
            conexao.commit()
            print("EMPATE!")

        conexao.commit()


    def verLider():
        cursor.execute("Select `nome`, `partidas`, `V`, `D`, `E`, `SG`, `pontos` from teste2 order by `pontos` desc limit 1 ")
        lider = cursor.fetchone()
        
        conexao.commit()
        dados = [["Nome", "Partidas", "V", "D", "E", "SG", "Pontos"],
                [lider[0], lider[1], lider[2], lider[3], lider[4], lider[5], lider[6]]]
        
        tabela = tabulate(dados, headers="firstrow", tablefmt="grid")
        print(tabela)
    
    def verRebaixados():
        cursor.execute("SELECT `nome` FROM teste2 ORDER BY pontos ASC LIMIT 4")
        rebaixados = cursor.fetchall()

        conexao.commit()

        dados = [rebaixados]

        tabela = tabulate(dados, headers="firstrow", tablefmt="grid")
        print(tabela)
        
        
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

while True:
    TabelaCampeonato.criarTabela()
    pergunta = int(input("Você deseja: \n1.Adicionar Times \n2.Executar Jogo \n3.Visualizar Tabela \n4.Ver Lider \n5.Ver Rebaixados \n6.Sair \n"))
    if (pergunta == 1):
        TabelaCampeonato.adicionarTime()
    
    elif (pergunta == 2):
        TabelaCampeonato.executarJogo()
    
    elif (pergunta == 3):
        TabelaCampeonato.visualizarTabela()
    
    elif (pergunta == 4):
        TabelaCampeonato.verLider()
    
    elif (pergunta == 5):
        TabelaCampeonato.verRebaixados()
    
    elif (pergunta == 6):
        print("Saindo...")
        break
        
