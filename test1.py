from funciones import saludar
import unittest

class TestCalculaMedia(unittest.TestCase):
    
    def test_1(self):
        resultado = saludar("David")
        self.assertEqual(resultado, "Hola David")

    def test_2(self):
        resultado = saludar("Juan")
        self.assertEqual(resultado, "Hola Juan")

if __name__ == '__main__':
    unittest.main()
