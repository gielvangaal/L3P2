# Voortgang – Data Engineering L3P2 (LU2)

Laatst bijgewerkt: 2026-11-09

## Doel

Bijhouden wat ik daadwerkelijk begrijp en zelfstandig kan toepassen, waar ik vastloop en wat ik later moet herhalen. De [toetsmatrijs](Toetsmatrijs_l3p2.md) is leidend. Werk dit bestand bij na betekenisvolle oefenmomenten, niet na iedere afzonderlijke vraag.

Statussen: **nieuw** / **oefenen** / **bijna beheerst** / **beheerst**. 'Beheerst' betekent: zonder hulp uitleggen én toepassen in een nieuwe situatie. Een status is geen beoordeling of cijfer.

## Startpositie

- **Fase:** voorbereiding / begin van de periode.
- **Voorkennis:** eerder gewerkt met BI, Power BI, datamodellering en ETL (LU1). Dat betekent niet automatisch dat machine learning of Python al beheerst wordt.
- **Python:** startniveau nog vast te stellen; begin bij de basis en laat mij zelf code schrijven.
- **Studiemodus:** voorlopig uitleg op hoofdlijnen (podcast/wandelen), géén overhoring totdat ik expliciet vraag om te oefenen. Ik geef zelf aan wanneer ik stop.
- **Overhoringen:** nog geen formele prestaties voor LU2 geregistreerd. Het eerste gesprek was oriënterend, geen nulmeting.
- **Praktijkopdracht:** document [Practicum en opdrachten – LU2](Practicum_en_opdrachten_overview_LU_2_2026_2027_v1.0.docx) globaal besproken. De hoofdeisen en deliverables zijn geïnventariseerd; projectkeuze en uitvoering moeten nog beginnen.

## Leerdoelen volgens toetsmatrijs

| Criterium | Weging | Status | Volgende aantoonbare stap |
| --- | ---: | --- | --- |
| Probleemanalyse, dataverzameling en voorbewerking | 20% | nieuw | Bedrijfsprobleem, dataset, datakwaliteit en eventuele bias kunnen onderbouwen |
| Supervised en/of unsupervised ML in Python | 20% | nieuw | Baseline bouwen en passende modelkeuze uitleggen |
| Statistische analyse en modeloptimalisatie | 20% | nieuw | Evaluatiemetriek kiezen, train/test correct scheiden, resultaten vergelijken |
| Interpretatie en verantwoording | 20% | nieuw | Modeluitkomsten vertalen naar het bedrijfsprobleem, met beperkingen |
| Complexiteit en technische uitvoering | 20% | nieuw | Reproduceerbare Python-uitvoering en onderbouwde technische keuzes |

## Onderwerpen om te oefenen

| Onderwerp | Status | Aantekeningen / misconcepties |
| --- | --- | --- |
| ML-basis: classificatie, regressie, clustering | oefenen | Eerste uitleg: regressie voorspelt getal, classificatie categorie; clustering ontdekt groepen zonder vooraf gegeven labels. Nog niet zelfstandig getoetst. |
| Supervised versus unsupervised learning | oefenen | Clustering correct herkend als unsupervised; supervised gebruikt voorbeelden met doeluitkomsten. Verder oefenen. |
| Data verkennen, cleaning, missing values en bias | nieuw | — |
| Python-basis, functies, modules en virtuele omgevingen | nieuw | — |
| pandas en datasets verwerken | nieuw | — |
| Train/test, datalekken en overfitting | nieuw | Nut van aparte testdata globaal besproken; nog geen technische verdieping of toetsing. |
| scikit-learn, baseline en modelvergelijking | nieuw | — |
| Statistiek en passende evaluatiemetrieken | nieuw | — |
| Modelverbetering en reproduceerbaarheid | nieuw | — |
| Resultaten interpreteren, onderbouwen en verantwoord omgaan met data/AI | nieuw | — |

## Praktijkopdracht – werkstatus

- **Document:** [Practicum_en_opdrachten_overview_LU_2_2026_2027_v1.0.docx](Practicum_en_opdrachten_overview_LU_2_2026_2027_v1.0.docx)
- **Opdrachtinhoud en formele eisen:** globaal doorgenomen: (1) Python-code/notebook voor datavoorbereiding, trainen en vergelijken van minimaal twee modellen; (2) werkend prototype met invoer en voorspelling; (3) rapport met analyse, evaluatie, verantwoording en reflectie. Individueel assessment van 25 minuten. Details blijven te toetsen aan het opdrachtdocument.
- **Aandachtspunt:** genoemde classificatiemetrieken (zoals confusion matrix, precision, recall en F1) sluiten niet direct aan op regressie; zo nodig met docent afstemmen.
- **Bedrijfsprobleem:** nog te bepalen.
- **Dataset:** nog te bepalen.
- **Eerste baseline / gekozen modellen:** nog niet gestart.
- **Evaluatie en optimalisatie:** nog niet gestart.
- **Rapportage / oplevering:** nog niet gestart; drie deliverables en assessment zijn wel in beeld.

## Oefenlog

### 2026-11-09 – eerste oriëntatie machine learning (gesprek)
- **Geoefend/besproken:** relatie met eerdere periode (data en BI), verschil regelgebaseerde software en ML, regressie/classificatie/clustering, supervised/unsupervised, data-kwaliteit, trainen, aparte testdata, evalueren en de globale workflow van probleem tot prototype. Korte zijstap naar AI/neuraal netwerk/taalmodel.
- **Zelfstandig goed:** benoemde dat ML patronen uit data leert in plaats van alleen expliciete regels te volgen; noemde slechte trainingsdata en ongeschikte modelinstellingen als risico; herkende clustering als unsupervised.
- **Fouten / misconcepties:** termen classificatie en labeling door elkaar; aanvankelijk onduidelijkheid over hoe AI, neurale netwerken en ML zich tot elkaar verhouden. Mondeling verduidelijkt, nog niet getoetst.
- **Uitleg nodig:** ja, uitdrukkelijk gevraagd om hoog-over uitleg in plaats van quizvragen. Nog niet begonnen met lezen.
- **Statuswijziging:** ML-basis en supervised/unsupervised van *nieuw* naar *oefenen*, niet naar beheerst.
- **Later herhalen:** drie taaktypen en onderscheid tussen leertypen, daarna features, target, trainen en train/test-splitsing.
- **Praktijk/Python:** geen code geschreven; project en dataset nog niet gekozen.
- **Afspraak:** voorlopig luistergerichte uitleg in kleine stappen; pas overhoren op eigen verzoek. Richting: relevante delen van *Machine Learning Foundations* (hoofdstuk 1 en 4.1–4.2) en *AI Ethics* (hoofdstuk 1–2) gericht lezen, niet noodzakelijk hele boeken.


Gebruik per betekenisvol oefenmoment dit compacte sjabloon:

### YYYY-MM-DD – onderwerp
- **Geoefend:** …
- **Zelfstandig goed:** …
- **Fouten / misconcepties:** …
- **Hint of uitleg nodig:** …
- **Statuswijziging:** …
- **Later herhalen:** …
- **Praktijk/Python:** …

## Eerstvolgende acties

1. Ga verder met hoog-over uitleg over hoe een model wordt getraind: features, target, trainingsvoorbeelden en testdata (huizenprijs als voorbeeld). Nog geen overhoring.
2. Lees gericht de voorgeschreven passages uit *Machine Learning Foundations* en later *AI Ethics*; bespreek onduidelijkheden tijdens wandelen.
3. Kies daarna een afgebakend bedrijfsprobleem en geschikte dataset; toets de formele opdrachteisen en eventuele deadlines nog zorgvuldig.
4. Zodra ik aangeef te willen oefenen: één vraag tegelijk, met feedback en herhaling. Begin later met Python-oefeningen en een werkende baseline.

> Houd dit document klein en feitelijk. Geen fictieve voortgang, geen automatisch 'beheerst' na één goed antwoord.
