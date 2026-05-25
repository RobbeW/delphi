## Gegeven

Een klas is geen volledig willekeurig netwerk. Leerlingen zitten in vriendengroepen, sportploegen of vaste projectgroepjes. Binnen zo'n cluster zijn er veel meer contacten dan tussen clusters.

In dit model kan elke besmette leerling in een cluster maximaal twee andere leerlingen besmetten. Een cluster kan natuurlijk niet meer besmettingen krijgen dan er nog vatbare leerlingen zijn.

## Gevraagd

* Vraag hoeveel clusters je onderzoekt en bewaar dit bijvoorbeeld in `aantal_clusters`.
* Vraag per cluster de `grootte` en het aantal `besmet` leerlingen.
* Bereken per cluster het aantal `vatbaar` leerlingen.
* Bereken hoeveel `nieuwe_besmettingen` ontstaan in die cluster.
* Print per cluster de nieuwe besmettingen en print daarna het totaal.

#### Rekenregel

Een besmette leerling besmet maximaal twee anderen. Daarom bereken je `besmet * 2`, maar je mag nooit meer nieuwe besmettingen tellen dan er vatbare leerlingen zijn. Gebruik dus `min(vatbaar, besmet * 2)`.

#### Voorbeeld

Voor deze invoer:
```
3
20
2
12
1
30
5
```

moet je programma exact dit printen:
```
Cluster 1: 4 nieuwe besmettingen
Cluster 2: 2 nieuwe besmettingen
Cluster 3: 10 nieuwe besmettingen
Totaal: 16 nieuwe besmettingen
```
