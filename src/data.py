"""Brondata inlezen en een eerste controle uitvoeren."""

from pathlib import Path

import pandas as pd


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "raw" / "primary_data_edited.csv"


def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    """Lees de semikolon-gescheiden primaire dataset in."""
    if not path.is_file():
        raise FileNotFoundError(
            f"Dataset ontbreekt: {path}\n"
            "Download primary_data_edited.csv en plaats het in data/raw/."
        )
    return pd.read_csv(path, sep=";")
