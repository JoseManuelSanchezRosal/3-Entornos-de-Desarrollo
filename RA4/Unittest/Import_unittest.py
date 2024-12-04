from Prueba_unittest import *
import unittest

class TestCalcularPrecioTotal(unittest.TestCase):
    def test_precio_positivo(self):
        self.assertEqual(calcular_precio_total(100, 0.21), 121)

    def test_precio_cero(self):
        self.assertEqual(calcular_precio_total(0, 0.21), 0)

    def test_precio_negativo(self):
        with self.assertRaises(ValueError):
                calcular_precio_total(-50, 0.21)
            

if __name__ == '__main__':
    unittest.main()