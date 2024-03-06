<<<<<<< HEAD
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
=======
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
>>>>>>> 9b894a910dc158995df5fb0a3eea6cc317f3c741
print(Carrinho.listaQuantidade)