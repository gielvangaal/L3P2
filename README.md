# L3P2 — Mushroom ML

Schoolproject Data Engineering (leeruitkomst 2): binaire classificatie van paddenstoelen op basis van de **Primary Mushroom Dataset**.

## Scope
- Verkenning van brondata (EDA)
- Synthetische voorbeelden genereren uit soortbeschrijvingen
- Data preprocessing en feature selection
- Decision Tree en Random Forest vergelijken
- Evaluatie: confusion matrix, accuracy, precision, recall, specificiteit en F1-score
- Een kleine Streamlit-interface die de opgeslagen scikit-learn Pipeline gebruikt

Dit is een **educatieve demonstratie**, geen hulpmiddel om de veiligheid van wilde paddenstoelen te beoordelen.

## Starten (PyCharm)
1. Clone de repository en open deze in PyCharm.
2. Maak een virtual environment aan en installeer de dependencies:
   ```bash
   python -m pip install -e .
   ```
3. Download `primary_data_edited.csv` van https://github.com/ghattab/secondarydata en plaats het in `data/raw/`. Bewaar de brondata ongewijzigd.
4. Start de eerste stap:
   ```bash
   python main.py
   ```
5. Later, nadat het getrainde model is opgeslagen:
   ```bash
   streamlit run app.py
   ```

## Opbouw
```text
data/raw/                 # oorspronkelijke dataset (zelf toevoegen)
data/processed/           # gegenereerde gegevens; niet committen
models/                   # opgeslagen model; niet committen
src/data.py               # inlezen en basisvalidatie
src/eda.py                # eerste data-verkenning
src/preprocessing.py      # voorbereiding en encoding (nog uitwerken)
src/synthetic.py          # synthetische datageneratie (nog uitwerken)
src/training.py           # training en Pipeline (nog uitwerken)
src/evaluation.py         # evaluatie van modellen (nog uitwerken)
main.py                   # regie over de ML-stappen
app.py                    # Streamlit-interface (later invullen)
```

## Uitgangspunten
- Train/test-split op **soortniveau** vóór het genereren van synthetische records.
- Geen informatie uit de testgroep gebruiken om training, encoding of kenmerkselectie af te stemmen.
- Laat brondata en gegenereerde data herkenbaar gescheiden.
- Genereer reproduceerbaar met een vaste random seed.
- Sla later een **getrainde** encoder en classifier gezamenlijk op in een scikit-learn Pipeline.
- Maak geen claims over betrouwbaarheid bij echte paddenstoelen op basis van synthetische testdata.

Bron: Wagner, D., Heider, D., & Hattab, G. (2021). *Mushroom data creation, curation, and simulation to support classification tasks*. Scientific Reports. https://doi.org/10.1038/s41598-021-87602-3
