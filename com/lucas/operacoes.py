import sys
class Operacoes():


    def multiplicacao(self, valores):
        val = 0
        for v in valores:
            val = val * v
        return val

    def divisao(self, valores):
        val = 0
        for v in valores:
            val = val / v
        return val