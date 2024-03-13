
i = 1

tabela = {
    "Flamengo": 85,
    "São paulo": 30,
    "Palmeiras": 84,
    "Avaí": 100
}

print("Time " + "Pontos")
for i in sorted(tabela, key = tabela.get, reverse=True):
    print(i, tabela[i])




