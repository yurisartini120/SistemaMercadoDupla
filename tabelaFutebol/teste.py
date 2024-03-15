from tabulate import tabulate

dados = [
    ["Nome", "Idade", "Profissão"],
    ["João", 25, "Engenheiro"],
    ["Maria", 30, "Advogada"],
    ["Carlos", 22, "Estudante"]
]

tabela = tabulate(dados, headers="firstrow", tablefmt="grid")

print(tabela)