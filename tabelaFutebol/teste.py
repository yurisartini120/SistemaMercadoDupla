import unittest
from unittest.mock import patch
from tarefaTestesKaua import TabelaCampeonato
import mysql.connector as mysql

class TestTabelaCampeonato(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Conectar ao banco de dados uma vez antes de todos os testes
        cls.conexao = mysql.connect(
            host='127.0.0.1',
            port=3306,
            database='teste',
            user='root',
            password=''
        )
        cls.cursor = cls.conexao.cursor()
        cls.tabela_campeonato = TabelaCampeonato()
        
    def test_criar_tabela(self):
        # Testar se a tabela é criada corretamente
        with patch.object(self.cursor, 'execute') as mock_execute:
            self.tabela_campeonato.criarTabela()
            mock_execute.assert_called_once_with("CREATE TABLE IF NOT EXISTS `teste2` (`id` int not null auto_increment primary key,`nome` varchar(255) not null, `partidas` int, `V` int, `D` int, `E` int, `SG` int, `pontos` int);")

    @patch('builtins.input', side_effect=['3', 'Time 1', 'Time 2', 'Time 3'])
    def test_adicionar_time(self, mock_input):
        # Testar se os times são adicionados corretamente
        self.tabela_campeonato.adicionarTime()
        self.cursor.execute("SELECT COUNT(*) FROM `teste2`")
        resultado = self.cursor.fetchone()
        self.assertEqual(resultado[0], 3)
        
    @patch('builtins.input', return_value='n')
    def test_visualizar_tabela(self, mock_input):
        # Testar se a visualização da tabela é realizada corretamente
        with patch('tarefaTestesKaua.cursor.fetchall', return_value=[('Time A', 10, 5, 3, 2, 10, 17)]):
            with patch('tarefaTestesKaua.tabulate.tabulate') as mock_tabulate:
                self.tabela_campeonato.visualizarTabela()
                mock_tabulate.assert_called_once()
    
    @patch('builtins.input', side_effect=['Time A', 'Time B'])
    @patch('random.choice', side_effect=[2, 1])
    def test_executar_jogo(self, mock_choice, mock_input):
        # Testar se a execução do jogo atualiza corretamente os pontos e estatísticas dos times
        self.tabela_campeonato.executarJogo()
        self.cursor.execute("SELECT `pontos` FROM `teste2` WHERE `nome`='Time A'")
        pontos_time_a = self.cursor.fetchone()[0]
        self.assertEqual(pontos_time_a, 3)
        self.cursor.execute("SELECT `pontos` FROM `teste2` WHERE `nome`='Time B'")
        pontos_time_b = self.cursor.fetchone()[0]
        self.assertEqual(pontos_time_b, 0)
        
    def test_ver_lider(self):
        # Testar se a função de visualização do líder é executada corretamente
        with patch('tabulate.tabulate') as mock_tabulate:
            self.tabela_campeonato.verLider()
            mock_tabulate.assert_called_once()
                
    def test_ver_rebaixados(self):
        # Testar se a função de visualização dos times rebaixados é executada corretamente
        with patch('tabulate.tabulate') as mock_tabulate:
            self.tabela_campeonato.verRebaixados()
            mock_tabulate.assert_called_once()

    @classmethod
    def tearDownClass(cls):
        # Fechar conexão ao banco de dados após todos os testes
        cls.conexao.close()

if __name__ == '__main__':
    unittest.main()
