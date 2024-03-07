import os
import time


perguntaUsuario = 1

class Carrinho:

    def __init__(self):
        self.listaProdutos = []
        self.listaPrecos = []
        self.listaQuantidade = []

    def adicionarProduto(self, produtoNome, produtoPreco, quantidadeProdutos):
        self.listaProdutos.append(produtoNome)
        self.listaPrecos.append(produtoPreco)
        self.listaQuantidade.append(quantidadeProdutos)

    def verProdutos(self, listaProdutos, listaQuantidade ):
        listaProdutos = (self.listaProdutos)
        print(listaProdutos)    
        listaQuantidade = (self.listaQuantidade)
        print(listaQuantidade)
        
        print("\n")     

    def removerProduto(self, numeroItem):
        self.listaProdutos.pop(numeroItem)
        self.listaPrecos.pop(numeroItem)
        self.listaQuantidade.pop(numeroItem)

    def calcularValorTotal(self):
        precoTotal = 0
        contadorProdutos = 0
        while (contadorProdutos < len(self.listaPrecos)):
            valorItem = self.listaPrecos[contadorProdutos]
            quantidadeItem = self.listaQuantidade[contadorProdutos]
            precoTotal+= valorItem*quantidadeItem
            contadorProdutos+=1
        print("O preço total é: " + str(precoTotal))
        return precoTotal


def finalizarSistema():
    print("Encerrando sistema...")
    quit()

if __name__ == '__main__':
    carrinho = Carrinho()

    while (perguntaUsuario != 5):
        try:
            os.system('cls')
            perguntaUsuario = int(input(" 1.Adicionar Produto ao carrinho \n 2.Ver produtos no carrinho \n 3.Remover Produto \n 4.Calcular preço total \n 5.Finalizar sistema \n Digite qual operação você deseja seguir: "))
            os.system('cls')
        
        except ValueError:

            print("Apenas números podem ser colocados! \n")

        else:

            if (perguntaUsuario == 1):
                produtoNome = input("Digite o nome do produto: ")
                try:
                    produtoPreco = float(input("Digite o preço do produto: "))
                    if produtoPreco <= 0:
                       print("Valor inválido!")
                       time.sleep(1)
                       continue
					   
                
                except ValueError:
                    print("Coloque um valor válido! \n")
                    time.sleep(1)
        
                else:
                    try:
                        quantidadeProdutos = int(input("Digite a quantidade de produtos: "))
                    except ValueError:
                        print("Coloque um valor válido! \n")
                    else:
                        carrinho.adicionarProduto(produtoNome=produtoNome, produtoPreco=produtoPreco, quantidadeProdutos=quantidadeProdutos)
                        print("Adicionado com sucesso!")
                        time.sleep(0.5)
                        os.system('cls')
                                
            
            elif(perguntaUsuario == 2):
                os.system('cls')
                carrinho.verProdutos(listaProdutos=carrinho.listaProdutos, listaQuantidade=carrinho.listaQuantidade )
                time.sleep(1) 

            
            elif(perguntaUsuario == 3):
                carrinho.verProdutos()
                try:
                    perguntaRemover = int(input("Digite o número do produto que quer remover (ex: 1, 2, 3, 4): "))
                    if(perguntaRemover > len(carrinho.listaProdutos)):
                        print("Coloque um número válido!")
                        time.sleep(0.5)
                except ValueError:
                    print("coloque um número válido!!")
                    time.sleep(0.5)
                else:
                    numeroItem = perguntaRemover-1
                    try:
                        carrinho.removerProduto(numeroItem=numeroItem)
                    except IndexError:
                        print("Não é possível remover!")
                        time.sleep(0.5)
                        os.system('cls')
                    else:
                        print("O produto "+str(perguntaRemover)+" foi removido com sucesso")
                        time.sleep(0.5)
                        os.system('cls')

            
            elif(perguntaUsuario == 4):

                quantidadeProdutosLista = (len(carrinho.listaProdutos))

                carrinho.calcularValorTotal()
                time.sleep(1.5)


            
            elif(perguntaUsuario == 5):
                carrinho.finalizarSistema()