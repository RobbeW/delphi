## Gegeven

Een SIR-model verdeelt een groep in drie delen: vatbaar, besmet en resistent. Per ronde kunnen besmette personen nieuwe mensen besmetten. Tegelijk genezen sommige besmette personen en worden ze resistent.

Je model hoeft niet medisch perfect te zijn. Het doel is om de drie aantallen correct bij te werken.

## Gevraagd

* Vraag het aantal vatbare, besmette en resistente personen.
* Vraag daarna hoeveel personen elke besmette persoon maximaal besmet, welk percentage geneest en hoeveel rondes je simuleert.
* Gebruik variabelen zoals `vatbaar`, `besmet`, `resistent`, `nieuwe_besmettingen` en `genezen`.
* Print na elke ronde de drie aantallen.

#### Rekenregel

Per ronde bereken je `nieuwe_besmettingen = min(vatbaar, besmet * besmettingskracht)`. Het aantal genezen personen is `math.floor(besmet * herstelpercentage / 100)`. Daarna werk je de drie groepen in deze volgorde bij: minder vatbaar, meer besmet door nieuwe besmettingen, minder besmet door herstel, meer resistent door herstel.

#### Voorbeeld

Voor deze invoer:
```
20
2
0
2
50
3
```

moet je programma exact dit printen:
```
Ronde 1: vatbaar=16, besmet=5, resistent=1
Ronde 2: vatbaar=6, besmet=13, resistent=3
Ronde 3: vatbaar=0, besmet=13, resistent=9
```
