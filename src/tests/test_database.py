import unittest
import database as db


class TestDatabase(unittest.TestCase):

    def test_cuadrante(self):
        self.assertEqual(db.Punto(2, 3).cuadrante(), None)
        self.assertEqual(db.Punto(-3, -1).cuadrante(), None)
        self.assertEqual(db.Punto(0, 0).cuadrante(), None)

    def test_vector(self):
        self.assertEqual(db.Punto(2, 3).vector(db.Punto(5, 5)), None)
        self.assertEqual(db.Punto(5, 5).vector(db.Punto(2, 3)), None)

    def test_distancia(self):
        self.assertEqual(db.Punto(2, 3).distancia(db.Punto(5, 5)), None)
        self.assertEqual(db.Punto(5, 5).distancia(db.Punto(2, 3)), None)

    def test_base(self):
        self.assertEqual(db.Rectangulo(db.Punto(2, 3), db.Punto(5, 5)).base(), None)

    def test_altura(self):
        self.assertEqual(db.Rectangulo(db.Punto(2, 3), db.Punto(5, 5)).altura(), None)

    def test_area(self):
        self.assertEqual(db.Rectangulo(db.Punto(2, 3), db.Punto(5, 5)).area(), None)


if __name__ == '__main__':
    unittest.main()