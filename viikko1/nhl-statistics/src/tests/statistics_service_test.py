import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())

    def test_etsii_oikean_pelaajan(self):
        pelaaja = self.stats.search("Kurri")
        self.assertEqual(pelaaja.name, "Kurri")

    def test_jos_pelaajaa_ei_loydy(self):
        pelaaja = self.stats.search("Teemu")
        self.assertIsNone(pelaaja)

    def test_etsii_oikean_joukkueen(self):
        joukkue = self.stats.team("PIT")
        self.assertAlmostEqual(joukkue[0].name, "Lemieux")

    def test_etsii_parhaan(self):
        paras = self.stats.top(1)
        self.assertAlmostEqual(paras[0].name, "Gretzky")