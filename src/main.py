from data_loader import load_raw_data, save_processed_data
from preprocessing import clean_data
from benford_analyzer import get_actual_distribution, get_benford_theoretical
from statistical_tests import mean_absolute_deviation
from visualization import generate_chart
import os

def main():
    # Création des dossiers si inexistants
    """
    Point d'entrée principal de l'application.

    Cette fonction crée les répertoires nécessaires et effectue les
    étapes suivantes :
    1. Charge les données brutes depuis 'president_county_candidate.csv'
    2. Nettoie les données
    3. Sauvegarde les données nettoyées dans 'cleaned_vote.csv'
    4. Calcule la distribution théorique de Benford
    5. Calcule la distribution réelle pour chaque candidat
    6. Calcule l'écart moyen absolu (MAD) entre les distributions réelle
       et théorique
    7. Affiche le MAD pour chaque candidat
    8. Génère un graphique comparant la distribution réelle avec la
       distribution théorique de Benford pour chaque candidat
    """
    for d in ['data/processed', 'data/results']: os.makedirs(d, exist_ok=True)

    # Workflow
    df = load_raw_data('president_county_candidate.csv')
    df_clean = clean_data(df)
    save_processed_data(df_clean, 'cleaned_votes.csv')
    
    theoretical = get_benford_theoretical()
    
    for candidate in ['Joe Biden', 'Donald Trump']:
        votes = df_clean[df_clean['candidate'] == candidate]['total_votes']
        actual = get_actual_distribution(votes)
        mad = mean_absolute_deviation(actual, theoretical)
        
        print(f"Candidat: {candidate} | MAD: {mad:.4f}")
        generate_chart(actual, theoretical, f"Analyse {candidate}", f"result_{candidate}.png")

if __name__ == "__main__":
    main()