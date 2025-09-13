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
    #Teste de subtração comum
    def test_subtracao(self):
        result = calculadora.sub(10,5)
        self.assertEqual(result,5)
    #Teste de subtração com zero
    def test_subtracaozero(self):
        result = calculadora.sub(7,0)
        self.assertEqual(result,7)
    #Teste de subtração com o subtraendo maior que o minuendo
    def test_subtracaominuendomaior(self):
        result = calculadora.sub(5,10)
        self.assertEqual(result,-5)
    #Teste de subtração com dois números negativos
    def test_subtracaodoisnegativos(self):
        result = calculadora.sub(-7,-9)
        self.assertEqual(result,2)
    #Teste de subtração com dois números grandes e com decimais
    def test_subtracaodoisgrandesdecimais(self):
        result = calculadora.sub(18490509.98,9476378.76)
        self.assertEqual(result,9014131.22)


############ MULTIPLICAÇÃO ###################

    #Teste de multiplicação comum
    def test_multi(self):
        result = calculadora.multi(10,5)
        self.assertEqual(result,50)
    #Teste de multiplicação por zero
    def test_multizero(self):
        result = calculadora.multi(10,0)
        self.assertEqual(result,0)
    #Teste de multiplicação com dóis números negativos
    def test_multinumnegativos(self):
        result = calculadora.multi(-5,-5)
        self.assertEqual(result,25)
    #Teste de multiplicação com dóis números grandes
    def test_multinumgrandes(self):
        result = calculadora.multi(1000000,1000000)
        self.assertEqual(result,1000000000000)
    #Teste de multiplicação com números decimais com precisão
    def test_multiprecisao(self):
        result = calculadora.multi(2.5,0.4)
        self.assertEqual(result,1.0)




############ DIVISÃO ###################

    #Teste de divisão comum
    def test_div(self):
        result = calculadora.div(10,5)
        self.assertEqual(result,2)
    #Teste de divisão com zero
    def test_divzero(self):
        result = calculadora.div(1,0)
        self.assertEqual(result,'Erro: divisão por zero')
    #Teste de divisão com dois números negativos
    def test_divdoisnegativos(self):
        result = calculadora.div(-10,-2)
        self.assertEqual(result,5)
    #Teste de divisão com decimais longos
    def test_divdeclongos(self):
        result = calculadora.div(1,3)
        self.assertEqual(result,0.3333333333333333)
    #Teste de divisão com o divisor maior que o dividendo
    def test_divisormaior(self):
        result = calculadora.div(2,5)
        self.assertEqual(result,0.4)