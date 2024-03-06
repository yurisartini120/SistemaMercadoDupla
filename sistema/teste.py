import os
import time

class Carrinho:
    listaProdutos = []
    listaPrecos = []
    listaQuantidade = []
    

produtoNome = input("Digite o nome do produto: ")
produtoPreco = float(input("Digite o preço do produto: "))
quantidadeProdutos = int(input("Digite a quantidade de produtos: "))

def Adicionar():
    
    print("Coloque um valor válido! \n")
    Carrinho.listaProdutos.append(produtoNome)
    Carrinho.listaPrecos.append(produtoPreco)
    Carrinho.listaQuantidade.append(quantidadeProdutos)



print(Adicionar())

print(Carrinho.listaProdutos)
print(Carrinho.listaPrecos)
print(Carrinho.listaQuantidade)