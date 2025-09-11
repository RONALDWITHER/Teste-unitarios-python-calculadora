import unittest
import calculadora

class TestCalculadora(unittest.TestCase):
    def test_adicaonumgrandes(self):
        result = calculadora.adicao(9874585684,263283783)
        self.assertEqual(result,10137869467)