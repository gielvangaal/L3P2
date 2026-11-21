"""Startpunt van de ML-workflow. Voorlopig alleen inlezen + eerste EDA."""

from src.data import load_data
from src.eda import summarize_data


def main() -> None:
    df = load_data()
    summarize_data(df)
    # TODO: preprocessing -> soort-split -> synthese -> encoding
    # TODO: trainen -> evalueren -> gekozen Pipeline opslaan


if __name__ == "__main__":
    main()
