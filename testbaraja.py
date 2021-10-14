import unittest
from baraja import Carta


class BarajaTest(unittest.TestCase):
    def test_crear_carta(self):
        carta = Carta(1, '1', 'trebol')
        self.assertEqual(carta.valor, 1)
        self.assertEqual(carta.simbolo, '1')
        self.assertEqual(carta.palo, 'trebol')

        carta = Carta(1523, 'asdfg', 'carta molona')
        self.assertEqual(carta.valor, 1523)
        self.assertNotEqual(carta.valor, 0)

    def test_valor_debe_ser_entero_positivo(self):
        with self.assertRaises(ValueError):
            Carta('1', 1, 12)
            Carta(-1, 12, 65)

    def test_baraja_carta(self):
        carta1 = Carta(1, '1', 'corazones')
        carta2 = Carta(1, '1', 'corazones')


if __name__ == '__main__':
    unittest.main()
