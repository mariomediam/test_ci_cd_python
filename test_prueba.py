from unittest import TestCase, skip
from prueba import sumatoria

class TestPruebas(TestCase):
    #@skip() 
    def testPrueba(self):
        numero = 10
        self.assertEqual(numero, 10)

    def testSumatoria(self):
        resultado = sumatoria(5,6)
        self.assertEqual(11, resultado)
        self.assertNotEqual(12, resultado)
    