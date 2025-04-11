import unittest
from Verificar_par import verifica_par

class TesteVerificaPar(unittest.TestCase):
    def test_verifica_par(self):
        self.assertTrue(verifica_par(2))
        self.assertFalse(verifica_par(3))
        self.assertTrue(verifica_par(0))
        self.assertTrue(verifica_par(-4))
