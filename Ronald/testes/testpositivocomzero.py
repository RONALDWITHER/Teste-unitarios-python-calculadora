import unittest
import calculadora

class TestCalculadora(unittest.TestCase):
    def test_adicaocomzero(self):
        result = calculadora.adicao(10,0)
        self.assertEqual(result,10)
