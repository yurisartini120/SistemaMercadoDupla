import unittest
import mercado

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.carrinho = mercado.Carrinho()
        
    def test_adicionar(self):
        self.carrinho.adicionarProduto(produtoNome="arroz", produtoPreco=-2, quantidadeProdutos=2)
       
        
        self.assertEqual(1, len(self.carrinho.listaPrecos))
        self.assertEqual(1, len(self.carrinho.listaProdutos))   
        self.assertEqual(1, len(self.carrinho.listaQuantidade)) 
        
    def test_remover(self):
        self.carrinho.adicionarProduto(produtoNome="arroz", produtoPreco=10, quantidadeProdutos=2)
        self.carrinho.removerProduto(numeroItem=0)

        self.assertEqual(0, len(self.carrinho.listaPrecos))
        self.assertEqual(0, len(self.carrinho.listaProdutos))   
        self.assertEqual(0, len(self.carrinho.listaQuantidade)) 
     
     
    def test_calcular(self):
        self.carrinho.adicionarProduto(produtoNome="arroz", produtoPreco=5, quantidadeProdutos=4)
        self.carrinho.adicionarProduto(produtoNome="feijao", produtoPreco=6, quantidadeProdutos=3)
        self.carrinho.adicionarProduto(produtoNome="carne", produtoPreco=7, quantidadeProdutos=2)
        
        valorTotal = self.carrinho.calcularValorTotal()
        self.assertEqual(52, valorTotal)

    

if __name__ == '__main__':
    unittest.main()