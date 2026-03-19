import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from benford_analyzer import extract_first_digit

def test_extract_first_digit():
    """
    Teste la fonction extract_first_digit.

    Vérifie que la fonction extrait correctement le premier chiffre d'un nombre donné.
    """
    assert extract_first_digit(123) == 1
    assert extract_first_digit(9876) == 9
    print("Test extract_first_digit: SUCCESS")

if __name__ == "__main__":
    test_extract_first_digit()