import os
import time


perguntaUsuario = 1

class Carrinho:
    listaProdutos = []
    listaPrecos = []
    listaQuantidade = []

    def adicionarProduto():
        Carrinho.listaProdutos.append(produtoNome)
        Carrinho.listaPrecos.append(produtoPreco)
        Carrinho.listaQuantidade.append(quantidadeProdutos)

    def verProdutos():
        print(Carrinho.listaProdutos)
        print(Carrinho.listaPrecos)
        print(Carrinho.listaQuantidade)
        print("\n")     

    def removerProduto():
        Carrinho.listaProdutos.pop(numeroItem)
        Carrinho.listaPrecos.pop(numeroItem)
        Carrinho.listaQuantidade.pop(numeroItem)

    def calcularValorTotal():
        precoTotal = 0
        contadorProdutos = 0
        while (contadorProdutos != quantidadeProdutosLista):
            valorItem = Carrinho.listaPrecos[contadorProdutos]
            quantidadeItem = Carrinho.listaQuantidade[contadorProdutos]
            precoTotal+= valorItem*quantidadeItem
            contadorProdutos+=1
        print("O preço total é: " + str(precoTotal))


    def finalizarSistema():
        print("Encerrando sistema...")
        quit()


try:

    perguntaIniciar = int(input("Iniciar Sistema \nDigite 1 para iniciar o sistema: "))
    os.system('cls')
except ValueError:
    print("Você inseriu errado!")
else:
    if (perguntaIniciar == 1):

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
                    except ValueError:
                        print("Coloque um valor válido! \n")
                        time.sleep(1)
                    else:
                        try:
                            quantidadeProdutos = int(input("Digite a quantidade de produtos: "))
                        except ValueError:
                            print("Coloque um valor válido! \n")
                        else:
                            Carrinho.adicionarProduto()
                            print("Adicionado com sucesso!")
                            time.sleep(0.5)
                            os.system('cls')
                                    
                
                elif(perguntaUsuario == 2):
                    os.system('cls')
                    Carrinho.verProdutos()
                    time.sleep(1) 

                
                elif(perguntaUsuario == 3):
                    Carrinho.verProdutos()
                    try:
                        perguntaRemover = int(input("Digite o número do produto que quer remover (ex: 1, 2, 3, 4): "))
                        if(perguntaRemover > len(Carrinho.listaProdutos)):
                            print("Coloque um número válido!")
                            time.sleep(0.5)
                    except ValueError:
                        print("coloque um número válido!!")
                        time.sleep(0.5)
                    else:
                        numeroItem = perguntaRemover-1
                        try:
                            Carrinho.removerProduto()
                        except IndexError:
                            print("Não é possível remover!")
                            time.sleep(0.5)
                            os.system('cls')
                        else:
                            print("O produto "+str(perguntaRemover)+" foi removido com sucesso")
                            time.sleep(0.5)
                            os.system('cls')

                
                elif(perguntaUsuario == 4):

                    quantidadeProdutosLista = (len(Carrinho.listaProdutos))

                    Carrinho.calcularValorTotal()
                    time.sleep(1.5)


                
                elif(perguntaUsuario == 5):
                    Carrinho.finalizarSistema()

    elif (perguntaIniciar != 1):
        print("Você é burro por acaso? Encerrando sistema")