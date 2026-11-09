# Voortgang – Data Engineering L3P2 (LU2)

Laatst bijgewerkt: 2026-11-09

## Doel

Bijhouden wat ik daadwerkelijk begrijp en zelfstandig kan toepassen, waar ik vastloop en wat ik later moet herhalen. De [toetsmatrijs](Toetsmatrijs_l3p2.md) is leidend. Werk dit bestand bij na betekenisvolle oefenmomenten, niet na iedere afzonderlijke vraag.

Statussen: **nieuw** / **oefenen** / **bijna beheerst** / **beheerst**. 'Beheerst' betekent: zonder hulp uitleggen én toepassen in een nieuwe situatie. Een status is geen beoordeling of cijfer.

## Startpositie

- **Fase:** voorbereiding / begin van de periode.
- **Voorkennis:** eerder gewerkt met BI, Power BI, datamodellering en ETL (LU1). Dat betekent niet automatisch dat machine learning of Python al beheerst wordt.
- **Python:** eerste mondelinge begrippentoets gedaan; praktische codevaardigheid nog niet vastgesteld.
- **Studiemodus:** bij nieuwe ML-stof eerst rustige uitleg; bij expliciet verzoek een korte overhoring, één vraag tegelijk. Ik geef zelf aan wanneer ik stop.
- **Overhoringen:** eerste mondelinge oefeningen voor ML en Python zijn hieronder per onderwerp vastgelegd; geen praktische vaardigheidstoets uitgevoerd.
- **Praktijkopdracht:** document [Practicum en opdrachten – LU2](Practicum_en_opdrachten_overview_LU_2_2026_2027_v1.0.docx) globaal besproken. De hoofdeisen en deliverables zijn geïnventariseerd; projectkeuze en uitvoering moeten nog beginnen.

## Leerdoelen volgens toetsmatrijs

| Criterium | Weging | Status | Volgende aantoonbare stap |
| --- | ---: | --- | --- |
| Probleemanalyse, dataverzameling en voorbewerking | 20% | nieuw | Bedrijfsprobleem, dataset, datakwaliteit en eventuele bias kunnen onderbouwen |
| Supervised en/of unsupervised ML in Python | 20% | nieuw | Baseline bouwen en passende modelkeuze uitleggen |
| Statistische analyse en modeloptimalisatie | 20% | nieuw | Evaluatiemetriek kiezen, train/test correct scheiden, resultaten vergelijken |
| Interpretatie en verantwoording | 20% | nieuw | Modeluitkomsten vertalen naar het bedrijfsprobleem, met beperkingen |
| Complexiteit en technische uitvoering | 20% | nieuw | Reproduceerbare Python-uitvoering en onderbouwde technische keuzes |

## Machine learning – kennis en voortgang

| Onderwerp | Status | Aantekeningen |
| --- | --- | --- |
| Regressie, classificatie en clustering | oefenen | Begrippen uitgelegd; clustering herkend als unsupervised. Nogmaals zelfstandig toepassen. |
| Supervised versus unsupervised | oefenen | Verschil op hoofdlijnen besproken. |
| Features en target | oefenen | Vier praktijkscenario's (bank, ziekenhuis, machine, school) grotendeels zelfstandig goed: target en relevante feature genoemd. |
| Van brondata via ETL naar trainingsdataset | oefenen | Verschil sterschema en platte ML-dataset begrepen; algoritme leert uit dataset en levert getraind model. |
| Data cleaning, datakwaliteit, missing values en bias | nieuw | Slechte data als risico genoemd; nog verder uitwerken. |
| Train/test, overfitting en datalekken | nieuw | Doel aparte testdata besproken, toepassing nog niet geoefend. |
| Modellen kiezen, evalueren en optimaliseren | nieuw | Nog niet praktisch geoefend. |
| Interpretatie, verantwoording en AI-ethiek | nieuw | Introductie besproken. |

**2026-11-09 – gesprek:** eerste oriëntatie op ML, supervised/unsupervised, regressie/classificatie/clustering, features/target en training; via voorbeelden de brug gelegd naar ETL en BI. Vier features/target-scenario's grotendeels correct; begrip groeit, nog niet beheerst. Geen ML-code geschreven.

**Volgende ML-stap:** rustig verder met trainingsvoorbeelden, train/test-splitsing en hoe een simpel model leert; later passende modellen vergelijken.

## Python – kennis en voortgang

| Onderwerp | Status | Aantekeningen |
| --- | --- | --- |
| List en dictionary | oefenen | Zelfstandig correct: list met items (ook geneste lijsten); dictionary met key-valueparen. |
| For-loop | oefenen | Zelfstandig: door elementen van een lijst lopen; uitbreiden naar andere iterables. |
| Functies | oefenen | Herbruikbaar codeblok met specifieke taak; definitie op verzoek aangescherpt. Parameters en return later oefenen. |
| `len()` | oefenen | Correct: aantal items in lijst. |
| `if/else` | oefenen | Correct: conditie bepaalt welk codeblok uitgevoerd wordt. |
| Variabelen | oefenen | Waarde/naam besproken; nauwkeuriger: naam verwijst naar object/waarde. |
| `input()` en stdin | oefenen | Eerst onbekend, daarna herkend als ingebouwde functie die tekst via standaardinvoer leest; geeft string terug. |
| String versus integer | oefenen | Correct: tekst versus geheel getal; ook cijfertekens kunnen in strings staan. |
| Zelf Python-code schrijven, modules, virtuele omgevingen, pandas en scikit-learn | nieuw | Nog geen praktische opdrachten uitgevoerd. |

**2026-11-09 – korte mondelinge overhoring:** list/dictionary, for-loop, functie, `len()`, if/else, variabelen en string/int grotendeels goed beantwoord; `input()` na uitleg begrepen. Dit toont herkenning en begrip, nog geen aantoonbare zelfstandige Python-implementatie.

**Volgende Python-stap:** korte begripsvragen blijven afwisselen met kleine eigen code-oefeningen; `input()`, functies met parameters/return en datatypes opnieuw toepassen.

## Praktijkopdracht – werkstatus

- **Document:** [Practicum_en_opdrachten_overview_LU_2_2026_2027_v1.0.docx](Practicum_en_opdrachten_overview_LU_2_2026_2027_v1.0.docx)
- **Opdrachtinhoud en formele eisen:** globaal doorgenomen: (1) Python-code/notebook voor datavoorbereiding, trainen en vergelijken van minimaal twee modellen; (2) werkend prototype met invoer en voorspelling; (3) rapport met analyse, evaluatie, verantwoording en reflectie. Individueel assessment van 25 minuten. Details blijven te toetsen aan het opdrachtdocument.
- **Aandachtspunt:** genoemde classificatiemetrieken (zoals confusion matrix, precision, recall en F1) sluiten niet direct aan op regressie; zo nodig met docent afstemmen.
- **Bedrijfsprobleem:** nog te bepalen.
- **Dataset:** nog te bepalen.
- **Eerste baseline / gekozen modellen:** nog niet gestart.
- **Evaluatie en optimalisatie:** nog niet gestart.
- **Rapportage / oplevering:** nog niet gestart; drie deliverables en assessment zijn wel in beeld.

## Eerstvolgende acties

1. Machine learning: training, features/target en train/test verder uitleggen, daarna toepassen.
2. Python: korte vragen en eigen mini-oefeningen met variabelen, functies, `input()` en datatypes.
3. Relevante delen van *Machine Learning Foundations* (hoofdstuk 1 en 4.1–4.2) en *AI Ethics* (hoofdstuk 1–2) gericht lezen.
4. Praktijkprobleem en dataset kiezen; later een eerste werkende baseline bouwen.

> Statussen blijven per onderdeel onafhankelijk. 'Beheerst' pas na uitleg zonder hulp én toepassing in een nieuwe situatie.
