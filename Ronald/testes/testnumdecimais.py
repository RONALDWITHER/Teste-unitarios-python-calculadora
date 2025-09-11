import unittest
import calculadora

class TestCalculadora(unittest.TestCase):
    def test_adicaofloat(self):
        result = calculadora.adicao(99.9,99.9)
        self.assertEqual(result,199.8)