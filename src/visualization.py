import matplotlib.pyplot as plt
import os

def generate_chart(actual, theoretical, title, filename):
    """
    Génère un graphique comparant la distribution réelle des chiffres avec la distribution théorique de Benford.

    Paramètres
    ----------
    actual : list
        Liste des fréquences réelles des chiffres
    theoretical : list
        Liste des fréquences théoriques des chiffres selon la loi de Benford
    title : str
        Titre du graphique
    filename : str
        Nom du fichier dans lequel sauvegarder le graphique

    Retours
    -------
    None
    """
    plt.figure(figsize=(10, 6))
    plt.bar(range(1, 10), actual, alpha=0.7, label='Réel', color='blue')
    plt.plot(range(1, 10), theoretical, marker='o', color='red', label='Benford')
    plt.title(title)
    plt.xlabel('Chiffre')
    plt.ylabel('Fréquence')
    plt.legend()
    plt.savefig(os.path.join('data', 'results', filename))
    plt.close()