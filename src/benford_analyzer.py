import numpy as np

# Extrait le premier chiffre d'un nombre
def extract_first_digit(number):
    """
    Extrait le premier chiffre d'un nombre.

    Paramètres
    ----------
    number : int
        Nombre dont on extrait le premier chiffre.

    Retours
    -------
    int
        Le premier chiffre du nombre, ou None si le nombre est vide ou nul.
    """
    s = str(number).strip().replace('.', '').lstrip('-0')
    return int(s[0]) if s else None

# Obtient la distribution réelle des premiers chiffres dans un jeu de données
def get_actual_distribution(data_series):
    """
    Calcule la distribution réelle des premiers chiffres dans un jeu de données.

    Paramètres
    ----------
    data_series : pd.Series
        Une Series pandas contenant les données pour calculer la distribution.

    Retours
    -------
    list
        Une liste de probabilités pour chaque chiffre de 1 à 9, dans l'ordre [1, 2, 3, 4, 5, 6, 7, 8, 9].
    """
    digits = data_series.apply(extract_first_digit).dropna()
    counts = digits.value_counts(normalize=True).sort_index()
    return [counts.get(d, 0) for d in range(1, 10)]

# Obtient la distribution théorique de Benford sous forme de liste de probabilités
def get_benford_theoretical():
    """
    Retourne la distribution théorique de Benford sous forme de liste de probabilités.

    La distribution de Benford est une distribution de probabilité pour le premier
    chiffre significatif d'un nombre. Elle est typiquement utilisée pour tester l'uniformité d'un jeu de données.

    Retours
    -------
    list
        Une liste de probabilités pour chaque chiffre de 1 à 9, dans
        l'ordre [1, 2, 3, 4, 5, 6, 7, 8, 9].
    """
    return [np.log10(1 + 1/d) for d in range(1, 10)]