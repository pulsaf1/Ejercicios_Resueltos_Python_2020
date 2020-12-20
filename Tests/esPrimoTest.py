import unittest
from Ejercicio8_1 import esPrimo

# Debemos crear una clase que hereda de la clase TestCase
class esPrimoTest(unittest.TestCase):

    # setUp se ejecuta siempre antes de ejecutar cada test
    def setUp(self):
        print("Empezando Test...")
    
    # tearDown se ejecuta siempre al finalizar cada test
    def tearDown(self):
        print("Test Ejecutado ...")
    
    # Cada test debe empezar por la palabra test_
    def test_entrynumber(self):
        self.assertTrue(esPrimo(7))
        self.assertFalse(esPrimo(8))
        self.assertEqual(esPrimo(3), True)
    
    def test_negative(self):
        self.assertFalse(esPrimo(-1))

    def test_isNotInt(self):
        self.assertFalse(esPrimo("Holaaa"))
        self.assertFalse(esPrimo("4"))

# Llamamos a main para que se ejecute el Runner.
if __name__ == '__main__':
    unittest.main()


