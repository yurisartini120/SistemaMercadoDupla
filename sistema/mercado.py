import os
import time

listaProdutos = []
listaPrecos = []
listaQuantidade = []
perguntaUsuario = 1

precoTotal = 0
contadorProdutos = 0

perguntaIniciar = int(input("Iniciar Sistema \nDigite 1 para iniciar o sistema: "))
os.system('cls')
if (perguntaIniciar == 1):

    while (perguntaUsuario != 5):
        perguntaUsuario = int(input(" 1.Adicionar Produto ao carrinho \n 2.Ver produtos no carrinho \n 3.Remover Produto \n 4.Calcular preço total \n 5.Finalizar sistema \n Digite qual operação você deseja seguir: "))
        os.system('cls')


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
                        listaProdutos.append(produtoNome)
                        listaPrecos.append(produtoPreco)
                        listaQuantidade.append(quantidadeProdutos)
                        os.system('cls')
            

                
        
        elif(perguntaUsuario == 2):
            os.system('cls')
            print(listaProdutos)
            print(listaPrecos)
            print(listaQuantidade)      

        
        elif(perguntaUsuario == 3):
            print(listaProdutos)

            try:
                perguntaRemover = int(input("Digite o número do produto que quer remover (ex: 1, 2, 3, 4): "))

            except ValueError:
                time.sleep(0.5)
                print("coloque um número correto!!")

            else:
                time.sleep(0.5)
                numeroItem = perguntaRemover-1
                print("O produto "+str(perguntaRemover)+" foi removido com sucesso")
                listaProdutos.pop(numeroItem)
                listaPrecos.pop(numeroItem)
                listaQuantidade.pop(numeroItem)
                os.system('cls')
            
            
        
        elif(perguntaUsuario == 4):

            quantidadeProdutosLista = (len(listaProdutos))

            while (contadorProdutos != quantidadeProdutosLista):
                valorItem = listaPrecos[contadorProdutos]
                quantidadeItem = listaQuantidade[contadorProdutos]
                precoTotal+= valorItem*quantidadeItem
                contadorProdutos+=1

            print("O preço total é: " + str(precoTotal))

        
        elif(perguntaUsuario == 5):
            break

elif (perguntaIniciar != 1):
    print("Você é burro por acaso? Encerrando sistema")