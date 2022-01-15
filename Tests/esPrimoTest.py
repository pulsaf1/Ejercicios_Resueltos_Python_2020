import unittest
from src.Ejercicio_Cap8_1 import esPrimo

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
        with self.assertRaises(TypeError):
            esPrimo(-1)

    def test_isNotInt(self):
        with self.assertRaises(TypeError):
            esPrimo("Holaaaa")
            esPrimo(False)


# Llamamos a main para que se ejecute el Runner.
if __name__ == '__main__':
    unittest.main()


