import time 
import random
from tabulate import tabulate

print("Casa X Desafiante")
time.sleep(1)
time1 = input("Time da casa:")
time.sleep(1)
time2 = input("Time Desafiante:")

print("------------------------------------------")
jogoIda = random.randint(1,3)
print("Jogo ida =", jogoIda)
jogoVolta = random.randint(1,3)
print("Jogo volta =", jogoVolta)
print("------------------------------------------")

pontuacao = jogoIda + jogoVolta
print("Pontuação final =" ,pontuacao)


class jogo:
    
    timeCasa = input("time da casa:")
    timeDesafiante = input("time desafiante:")
    pontos = 0


    golsCasa = random.randint(1,3)
    golsDesafiante = random.randint(1,3)

    time.sleep(0.5)
    print("------------------------------------------")
    print(golsCasa, "X", golsDesafiante)
    time.sleep(0.5)
    if (golsCasa > golsDesafiante):
        print(timeCasa, "Vencedor com ",golsCasa, "GOLS")
        pontos += 3
        print("pontuação: +", pontos)
    elif(golsCasa == golsDesafiante):
        print("Empate!")
        pontos += 1
        print("pontuação para ambos: +", pontos)
    elif(golsDesafiante > golsCasa):
        print(timeDesafiante, "Vencedor com ",golsDesafiante, "GOLS")
        pontos += 3
        print("pontuação: +", pontos)
    print("------------------------------------------")


    
        
lista = [
    
    ["Times", "vitorias", "mundial"],
    ["São Paulo", 688, 3],
    ["Flamengo", 671, 2],
    ["Palmeiras", 3457, 0]
]

print(tabulate(lista, headers= 'firstrow'))

