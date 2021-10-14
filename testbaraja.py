import unittest

from baraja import Carta


class BarajaTest(unittest.TestCase):
    def test_baraja_carta(self):
        carta1 = Carta(1, '1', 'corazones')
        carta2 = Carta(1, '1', 'corazones')
