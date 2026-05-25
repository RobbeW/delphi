## Gegeven

Tijdens een schooldag hebben leerlingen niet in elke les dezelfde contacten. Toch kun je een eenvoudige simulatie maken door per klas en per les het aantal besmettingen bij te werken.

Elke les kan elke besmette leerling een vast aantal nieuwe leerlingen besmetten, zolang er nog leerlingen vatbaar zijn.

## Gevraagd

* Vraag het aantal klassen, het aantal lessen, de klasgrootte en het aantal startbesmettingen per klas.
* Gebruik geneste lussen: een lus voor de klassen en een lus voor de lessen.
* Gebruik variabelen zoals `besmet`, `vatbaar`, `nieuwe_besmettingen` en `totaal_school`.
* Print per klas hoeveel leerlingen na alle lessen besmet zijn.
* Print op het einde het totaal aantal besmettingen op school.

#### Rekenregel

Per les kan elke besmette leerling een nieuwe leerling besmetten. Daarom is `nieuwe_besmettingen = min(vatbaar, besmet)`. Daarna tel je die nieuwe besmettingen bij `besmet` en trek je ze af van `vatbaar`.

#### Voorbeeld

Voor deze invoer:
```
2
3
24
2
```

moet je programma exact dit printen:
```
Klas 1: 16 besmet na 3 lessen
Klas 2: 16 besmet na 3 lessen
Totaal op school: 32 besmettingen
```
