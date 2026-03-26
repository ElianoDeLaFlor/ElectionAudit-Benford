import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from statistical_tests import mean_absolute_deviation

class TestStatisticalTests(unittest.TestCase):
    def test_mean_absolute_deviation(self):
        """Teste le calcul de l'écart moyen absolu (MAD)"""
        actual = [0.3, 0.2, 0.5]
        theoretical = [0.3, 0.2, 0.5]
        
        # MAD = (|0.3 - 0.3| + |0.2 - 0.2| + |0.5 - 0.5|) / 3
        #     = (0 + 0 + 0) / 3
        #     = 0
        expected_mad = 0
        
        mad = mean_absolute_deviation(actual, theoretical)
        self.assertAlmostEqual(mad, expected_mad)

if __name__ == '__main__':
    unittest.main()
