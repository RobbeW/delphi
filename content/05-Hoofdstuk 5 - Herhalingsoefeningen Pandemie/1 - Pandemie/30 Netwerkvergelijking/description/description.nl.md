## Gegeven

Twee netwerken kunnen evenveel personen hebben en toch heel anders verspreiden. In een gelijk netwerk heeft iedereen ongeveer evenveel contacten. In een ongelijk netwerk heeft een hub veel meer contacten dan de gewone personen.

Je vergelijkt beide netwerken ronde per ronde.

## Gevraagd

* Vraag het aantal personen, het aantal rondes, het aantal contacten in het gelijke netwerk, het aantal contacten van de hub en het aantal contacten van gewone personen in het ongelijke netwerk.
* Gebruik variabelen zoals `gelijk_besmet`, `ongelijk_besmet`, `hub_contacten` en `gewone_contacten`.
* Print per ronde het totaal besmette personen in beide netwerken.
* Zorg ervoor dat het aantal besmettingen nooit groter wordt dan het aantal personen.
* Vergelijk op het einde welk netwerk sneller verspreidt.

#### Rekenregel

Het gelijke netwerk krijgt per ronde `gelijk_besmet * gelijke_contacten // 10` nieuwe besmettingen. Het ongelijke netwerk gebruikt de hub apart: `(hub_contacten + (ongelijk_besmet - 1) * gewone_contacten) // 10`. Gebruik telkens `min(personen - besmet, nieuwe_besmettingen)`, zodat je nooit boven het aantal personen gaat.

#### Voorbeeld

Voor deze invoer:
```
100
3
3
20
1
```

moet je programma exact dit printen:
```
Ronde 1: gelijk=1, ongelijk=3
Ronde 2: gelijk=1, ongelijk=5
Ronde 3: gelijk=1, ongelijk=7
Het ongelijke netwerk verspreidt sneller.
```
