import unittest
import calculadora

class TestCalculadora(unittest.TestCase):

############ ADICÃO ###################
    #Teste de adição comum
    def test_adicao(self):
        result = calculadora.adicao(10,5)
        self.assertEqual(result,15)
    #Teste com número negativo
    def test_adicaonegativo(self):
        result = calculadora.adicao(-9,1)
        self.assertEqual(result,-8)
    #Teste com Números Grandes
    def test_adicaonumgrandes(self):
        result = calculadora.adicao(9874585684,263283783)
        self.assertEqual(result,10137869467)
    #Teste com Números com casa decimais
    def test_adicaofloat(self):
        result = calculadora.adicao(99.9,99.9)
        self.assertEqual(result,199.8)
    #Teste número positivo com zero.  
    def test_adicaocomzero(self):
        result = calculadora.adicao(10,0)
        self.assertEqual(result,10)

############ SUBTRAÇÃO ###################
    def test_subtracao(self):
        result = calculadora.sub(10,5)
        self.assertEqual(result,5)

############ MULTIPLICAÇÃO ###################

    def test_multi(self):
        result = calculadora.multi(10,5)
        self.assertEqual(result,50)

############ DIVISÃO ###################
    def test_div(self):
        result = calculadora.div(10,5)
        self.assertEqual(result,2)