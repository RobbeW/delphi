## Gegeven

Een virus blijft niet altijd in dezelfde stad. Reizigers kunnen besmettingen meenemen naar een volgende stad, waar opnieuw lokale verspreiding ontstaat.

Je volgt een virus door meerdere steden. In elke stad bereken je lokale besmettingen en daarna hoeveel besmette reizigers verder trekken.

## Gevraagd

* Vraag het aantal steden, het startaantal besmette reizigers, de lokale groeifactor en het reispercentage.
* Gebruik variabelen zoals `reizigers`, `lokale_besmettingen`, `totaal` en `stad`.
* Print per stad het aantal lokale besmettingen en het totaal.
* Bereken na elke stad hoeveel besmette personen verder reizen.
* Print die reisbeweging voor elke stad behalve de laatste.

#### Rekenregel

In elke stad bereken je `lokale_besmettingen = math.floor(reizigers * r0)`. Het totaal in die stad is `reizigers + lokale_besmettingen`. Daarna reist `math.floor(totaal * reispercentage / 100)` verder naar de volgende stad. Als er besmettingen zijn maar die berekening 0 reizigers geeft, reist er toch 1 besmette persoon verder.

#### Voorbeeld

Voor deze invoer:
```
4
5
1.5
25
```

moet je programma exact dit printen:
```
Stad 1: 7 lokale besmettingen, 12 totaal
Naar stad 2 reizen 3 besmette personen.
Stad 2: 4 lokale besmettingen, 7 totaal
Naar stad 3 reizen 1 besmette personen.
Stad 3: 1 lokale besmettingen, 2 totaal
Naar stad 4 reizen 1 besmette personen.
Stad 4: 1 lokale besmettingen, 2 totaal
```
