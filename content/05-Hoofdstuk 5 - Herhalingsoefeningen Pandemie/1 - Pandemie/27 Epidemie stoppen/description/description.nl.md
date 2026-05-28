## Gegeven

Een epidemie stopt pas wanneer elke besmette persoon gemiddeld minder dan een nieuwe persoon besmet. Dat betekent dat de effectieve `R` onder 1 moet zakken.

Vaccinatie verlaagt het vatbare deel van de bevolking. Je zoekt hoeveel vaccinatierondes nodig zijn om `R` onder 1 te krijgen.

## Gevraagd

* Vraag `r0`, de grootte van de bevolking en het aantal vaccinaties per ronde.
* Gebruik variabelen zoals `gevaccineerd`, `ronde`, `vatbaar_deel` en `effectieve_r`.
* Print eerst de startsituatie.
* Vaccineer ronde per ronde bij zolang de effectieve `R` minstens 1 is.
* Print na elke ronde het aantal gevaccineerden en de nieuwe `R`.
* Print op het einde na hoeveel rondes de epidemie stopt.
* Als `R` bij de start al kleiner is dan 1, stopt de epidemie na 0 vaccinatierondes.

#### Rekenregel

Na elke vaccinatieronde bereken je welk deel van de bevolking nog vatbaar is: `1 - gevaccineerd / populatie`. De nieuwe R is `r0 * (1 - gevaccineerd / populatie)`, afgerond op twee decimalen. Zodra die waarde kleiner is dan 1, stopt de epidemie in dit model.

#### Voorbeeld

Voor deze invoer:
```
2.5
1200
100
```

moet je programma exact dit printen:
```
Start: 0 gevaccineerd, R = 2.5
Ronde 1: 100 gevaccineerd, R = 2.29
Ronde 2: 200 gevaccineerd, R = 2.08
Ronde 3: 300 gevaccineerd, R = 1.88
Ronde 4: 400 gevaccineerd, R = 1.67
Ronde 5: 500 gevaccineerd, R = 1.46
Ronde 6: 600 gevaccineerd, R = 1.25
Ronde 7: 700 gevaccineerd, R = 1.04
Ronde 8: 800 gevaccineerd, R = 0.83
De epidemie stopt na 8 vaccinatierondes.
```
