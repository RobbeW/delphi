## Gegeven

Niet alleen virussen verspreiden zich. Ook challenges, geruchten en memes kunnen viraal gaan. Elke deelnemer kan nieuwe deelnemers aantrekken.

Je simuleert een challenge die elke dag meer mensen bereikt, maar je stopt zodra de challenge viraal is of het aantal dagen voorbij is.

## Gevraagd

* Vraag het startaantal deelnemers, de vermenigvuldigingsfactor, het aantal dagen en de virale grens.
* Gebruik variabelen zoals `deelnemers`, `nieuwe_deelnemers`, `dag` en `grens`.
* Bereken per dag hoeveel nieuwe deelnemers erbij komen.
* Print per dag het aantal nieuwe deelnemers en het totaal.
* Print op het einde of de challenge viraal ging of hoeveel mensen bereikt zijn.

#### Rekenregel

Elke dag bereken je eerst `nieuwe_deelnemers = math.floor(huidig * factor)`. Die nieuwe deelnemers tel je bij `totaal`. Daarna worden de nieuwe deelnemers de groep die de volgende dag opnieuw mensen kan overtuigen.

#### Voorbeeld

Voor deze invoer:
```
10
3
3
500
```

moet je programma exact dit printen:
```
Dag 1: 30 nieuwe deelnemers, 40 totaal
Dag 2: 90 nieuwe deelnemers, 130 totaal
Dag 3: 270 nieuwe deelnemers, 400 totaal
Na 3 dagen zijn er 400 deelnemers bereikt.
```
