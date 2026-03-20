from data_loader import load_raw_data, save_processed_data
from preprocessing import clean_data
from benford_analyzer import get_actual_distribution, get_benford_theoretical
from statistical_tests import mean_absolute_deviation
from visualization import generate_chart
import os
import pandas as pd

def process_file(file_name):
    df = load_raw_data(file_name)
    df_clean = clean_data(df)
    
    # Save processed file with a suffix indicating the input file
    base_name = os.path.splitext(file_name)[0]
    processed_name = f"cleaned_{base_name}.csv"
    save_processed_data(df_clean, processed_name)
    
    theoretical = get_benford_theoretical()
    
    print(f"\n--- Analyse des données: {file_name} ---")
    for candidate in ['Joe Biden', 'Donald Trump']:
        # Ensure we don't fail if a candidate isn't present
        votes = df_clean[df_clean['candidate'] == candidate]['total_votes']
        if len(votes) == 0:
            continue
            
        actual = get_actual_distribution(votes)
        mad = mean_absolute_deviation(actual, theoretical)
        
        print(f"Candidat: {candidate} | MAD: {mad:.4f}")
        generate_chart(actual, theoretical, f"Analyse {candidate} ({base_name})", f"result_{candidate}_{base_name}.png")
        
        # Sauvegarde des données de la distribution
        df_dist = pd.DataFrame({
            'Chiffre': range(1, 10),
            'Distribution_Reelle': actual,
            'Distribution_Theorique': theoretical
        })
        csv_filename = os.path.join('data', 'results', f"distribution_{candidate}_{base_name}.csv")
        df_dist.to_csv(csv_filename, index=False)

def main():
    # Création des dossiers si inexistants
    """
    Point d'entrée principal de l'application.

    Cette fonction crée les répertoires nécessaires et effectue les
    étapes suivantes pour chaque fichier de données :
    1. Charge les données brutes
    2. Nettoie les données
    3. Sauvegarde les données nettoyées
    4. Calcule la distribution théorique de Benford
    5. Calcule la distribution réelle pour chaque candidat
    6. Calcule l'écart moyen absolu (MAD) entre les distributions
    7. Affiche le MAD pour chaque candidat
    8. Génère un graphique comparant les distributions
    """
    for d in ['data/processed', 'data/results']: os.makedirs(d, exist_ok=True)

    # Workflow pour les deux fichiers de données
    files_to_process = ['president_county_candidate.csv', 'president_state.csv']
    
    for file_name in files_to_process:
        process_file(file_name)

if __name__ == "__main__":
    main()