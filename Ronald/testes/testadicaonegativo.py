import unittest
import calculadora

class TestCalculadora(unittest.TestCase):
    def test_adicaonegativo(self):
        result = calculadora.adicao(-9,1)
        self.assertEqual(result,-8)