import unittest
import punto as pt


class TestEjercicio2(unittest.TestCase):
    def test_punto(self):
        punto1 = pt.Punto(2, 3)
        self.assertEqual(punto1.x, 2)
        self.assertEqual(punto1.y, 3)

    def test_cuadrante(self):
        punto1 = pt.Punto(2, 3)
        self.assertEqual(pt.Punto.cuadrante(punto1), "El punto se encuentra en el primer cuadrante")

    def test_vector(self):
        punto1 = pt.Punto(2, 3)
        punto2 = pt.Punto(5, 5)
        self.assertEqual(pt.Punto.vector(punto1, punto2), f'El vector entre los puntos es (3, 2)')

    def test_distancia(self):
        punto1 = pt.Punto(2, 3)
        punto2 = pt.Punto(5, 5)
        self.assertEqual(pt.Punto.distancia(punto1, punto2), f'La distancia entre los puntos es 3.605551275463989 unidades')

    
    def test_rectangulo(self):
        punto1 = pt.Punto(2, 3)
        punto2 = pt.Punto(5, 5)
        rectangulo = pt.Rectangulo(punto1, punto2)
        self.assertEqual(rectangulo.punto1.x, 2)
        self.assertEqual(rectangulo.punto1.y, 3)
        self.assertEqual(rectangulo.punto2.x, 5)
        self.assertEqual(rectangulo.punto2.y, 5)

    def test_base(self):
        punto1 = pt.Punto(2, 3)
        punto2 = pt.Punto(5, 5)
        rectangulo = pt.Rectangulo(punto1, punto2)
        self.assertEqual(pt.Rectangulo.base(rectangulo), f'La base del rectángulo es 3 unidades')

    def test_altura(self):
        punto1 = pt.Punto(2, 3)
        punto2 = pt.Punto(5, 5)
        rectangulo = pt.Rectangulo(punto1, punto2)
        self.assertEqual(pt.Rectangulo.altura(rectangulo), f'La altura del rectángulo es 2 unidades')

    def test_area(self):
        punto1 = pt.Punto(2, 3)
        punto2 = pt.Punto(5, 5)
        rectangulo = pt.Rectangulo(punto1, punto2)
        self.assertEqual(pt.Rectangulo.area(rectangulo), f'El área del rectángulo es 6 unidades cuadradas')
