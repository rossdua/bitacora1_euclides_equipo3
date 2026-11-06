import unittest
from mcd_algoritmo import mcd_euclides

class TestMcdEuclides(unittest.TestCase):
    def test_mcd_valores_positivos(self):
        self.assertEqual(mcd_euclides(48, 18)[0], 6)
        self.assertEqual(mcd_euclides(101, 10)[0], 1)

    def test_mcd_con_negativos(self):
        self.assertEqual(mcd_euclides(-48, 18)[0], 6)
        self.assertEqual(mcd_euclides(48, -18)[0], 6)
        self.assertEqual(mcd_euclides(-48, -18)[0], 6)

    def test_mcd_con_cero(self):
        self.assertEqual(mcd_euclides(5, 0)[0], 5)
        self.assertEqual(mcd_euclides(0, 5)[0], 5)

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)

