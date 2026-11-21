"""Eerste verkenning van de ongewijzigde brondata."""

import pandas as pd


def summarize_data(df: pd.DataFrame) -> None:
    """Toon omvang, kolomnamen, ontbrekende waarden en klassenverdeling."""
    print(f"Records: {len(df)} | Kolommen: {len(df.columns)}")
    print("\nKolommen:")
    print(df.columns.tolist())
    print("\nOntbrekende waarden per kolom:")
    print(df.isna().sum().to_string())
    if "class" in df.columns:
        print("\nKlassenverdeling:")
        print(df["class"].value_counts(dropna=False).to_string())
