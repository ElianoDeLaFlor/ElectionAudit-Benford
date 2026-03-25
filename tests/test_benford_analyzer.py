import unittest
import pandas as pd
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from benford_analyzer import extract_first_digit, get_actual_distribution, get_benford_theoretical

class TestBenfordAnalyzer(unittest.TestCase):
    def test_extract_first_digit(self):
        """Teste l'extraction du premier chiffre pour divers types de nombres."""
        self.assertEqual(extract_first_digit(123), 1)
        self.assertEqual(extract_first_digit(9876), 9)
        self.assertEqual(extract_first_digit(0.56), 5)
        self.assertEqual(extract_first_digit("0.089"), 8)
        self.assertIsNone(extract_first_digit(0))
        self.assertIsNone(extract_first_digit("0.00"))

    def test_get_actual_distribution(self):
        """Teste le calcul de la distribution réelle."""
        # Séries de données : 10, 15, 20, 30, 40, 50, 60, 70, 80, 90
        # Premiers chiffres correspondants : 1, 1, 2, 3, 4, 5, 6, 7, 8, 9
        # Proba : 1 -> 0.2, les autres de 2 à 9 -> 0.1
        data = pd.Series([10, 15, 20, 30, 40, 50, 60, 70, 80, 90])
        dist = get_actual_distribution(data)
        
        self.assertEqual(len(dist), 9)
        self.assertAlmostEqual(dist[0], 0.2)
        for i in range(1, 9):
            self.assertAlmostEqual(dist[i], 0.1)

    def test_get_benford_theoretical(self):
        """Teste le calcul de la distribution théorique de Benford."""
        dist = get_benford_theoretical()
        
        self.assertEqual(len(dist), 9)
        # La somme des probabilités doit être 1
        self.assertAlmostEqual(sum(dist), 1.0)
        # Vérification des valeurs de Benford p(d) = log10(1 + 1/d)
        self.assertAlmostEqual(dist[0], np.log10(1 + 1/1))  # Pour 1
        self.assertAlmostEqual(dist[8], np.log10(1 + 1/9))  # Pour 9

if __name__ == '__main__':
    unittest.main()