from unittest import TestCase
from com.lucas.operacoes import Operacoes

class TestOperacaoes(TestCase):
    def setUp(self):
        self.operacoes = Operacoes()
    
    def test_multiplicacao(self):
        self.assertEqual(self.operacoes.multiplicacao([5,5]), 25, "Deveria ser 25")
        
    def test_divisao(self):
        self.assertEqual(self.operacoes.divisao([25,5]), 5, "Deveria ser 5")
        