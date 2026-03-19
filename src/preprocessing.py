def clean_data(df):
    # Filtrer Biden et Trump
    """
    Nettoie un DataFrame contenant les données des élections présidentielles américaines.

    Paramètres
    ----------
    df : pd.DataFrame
        DataFrame contenant les données des élections

    Retours
    -------
    df_filtered : pd.DataFrame
        DataFrame contenant uniquement les lignes pour Biden et Trump, avec des votes > 0
    """
    df_filtered = df[df['candidate'].isin(['Joe Biden', 'Donald Trump'])].copy()
    # Garder les votes significatifs (>0)
    df_filtered = df_filtered[df_filtered['total_votes'] > 0]
    return df_filtered