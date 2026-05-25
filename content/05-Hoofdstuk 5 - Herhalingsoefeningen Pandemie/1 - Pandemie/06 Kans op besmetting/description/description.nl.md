## Gegeven

Niet elk contact leidt tot een besmetting. Daarom simuleren we elk contact apart. Voor elk contact trekt het programma een willekeurig getal van 1 tot en met 100.

Ligt dat getal kleiner dan of gelijk aan de besmettingskans, dan raakt die persoon besmet.

## Gevraagd

* Vraag het aantal contacten en de besmettingskans in procent.
* Gebruik `random.randint(1, 100)` voor elk contact.
* Tel met variabelen zoals `besmet` en `niet_besmet` hoeveel contacten besmet raken.
* Print op het einde beide aantallen.

#### Rekenregel

Een willekeurig getal kleiner dan of gelijk aan de besmettingskans telt als besmetting. Bij een kans van 30 raakt een contact dus besmet als `worp <= 30`.

#### Voorbeeld

Voor deze invoer:
```
8
30
```

kan je programma bijvoorbeeld dit printen:
```
Besmet: 3
Niet besmet: 5
```
