import unittest
import calculadora

class TestCalculadora(unittest.TestCase):
    def test_adicao(self):
        result = calculadora.adicao(10,5)
        self.assertEqual(result,15)