import pandas as pd
import os

# Charge les données brutes depuis un fichier
def load_raw_data(file_name):
    """
    Charge les données brutes depuis un fichier.

    Paramètres
    ----------
    file_name : str
        Nom du fichier à charger.

    Retours
    -------
    df : pandas.DataFrame
        DataFrame contenant les données chargées.
    """
    path = os.path.join('data', 'raw', file_name)
    return pd.read_csv(path)

# Sauvegarde les données traitées dans un fichier
def save_processed_data(df, file_name):
    path = os.path.join('data', 'processed', file_name)
    df.to_csv(path, index=False)