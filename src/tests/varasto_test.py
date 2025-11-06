import unittest
from varasto import Varasto

class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)



    def test_negatiivinen_tilavuus_nollataan(self):
        v = Varasto(-5)
        self.assertEqual(v.tilavuus, 0)
        self.assertEqual(v.saldo, -5)



    def test_negatiivinen_alkusaldo_nollataan(self):
        v = Varasto(10, -2)
        self.assertEqual(v.saldo, 0)


    def test_alkusaldo_yli_tilavuuden_rajoittuu(self):
        v = Varasto(10, 15)
        self.assertEqual(v.saldo, 10)



    def test_ota_negatiivinen_palauttaa_nolla_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(5)
        saatu = self.varasto.ota_varastosta(-3)
        self.assertEqual(saatu, 0.0)
        self.assertEqual(self.varasto.saldo, 5)



    def test_ota_yli_saldon_palauttaa_kaiken_ja_nollaa_saldon(self):
        self.varasto.lisaa_varastoon(5)
        saatu = self.varasto.ota_varastosta(10)
        self.assertEqual(saatu, 5)
        self.assertEqual(self.varasto.saldo, 0)



    def test_ota_normaalisti_vahentaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        saatu = self.varasto.ota_varastosta(3)
        self.assertEqual(saatu, 3)
        self.assertEqual(self.varasto.saldo, 5)


    def test_str_palauttaa_oikean_merkkijonon(self):
        self.varasto.lisaa_varastoon(4)
        s = str(self.varasto)
        self.assertIn("saldo = 4", s)
        self.assertIn("tilaa 6", s)


    def test_lisaa_negatiivinen_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.lisaa_varastoon(-3)
        self.assertEqual(self.varasto.saldo, 5)  

    def test_lisaa_yli_tilavuuden_tayttaa_varaston(self):
        self.varasto.lisaa_varastoon(15)
        self.assertEqual(self.varasto.saldo, 10)
