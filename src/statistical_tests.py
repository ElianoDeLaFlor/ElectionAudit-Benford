import numpy as np

def mean_absolute_deviation(actual, theoretical):
    """
    Calcule l'écart moyen absolu (MAD) entre les distributions réelle et théorique.

    Paramètres
    ----------
    actual : list
        Distribution réelle des premiers chiffres
    theoretical : list
        Distribution théorique des premiers chiffres

    Retours
    -------
    float
        Écart moyen absolu entre les distributions réelle et théorique
    """
    return np.mean(np.abs(np.array(actual) - np.array(theoretical)))