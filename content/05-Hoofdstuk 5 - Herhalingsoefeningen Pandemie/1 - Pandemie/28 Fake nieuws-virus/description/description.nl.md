## Gegeven

Geruchten kunnen zich gedragen als een virus. Wie het gerucht gelooft, kan het doorgeven aan anderen. Factchecks kunnen de verspreiding afremmen.

Je simuleert de verspreiding ronde per ronde en stopt als het gerucht viraal gaat of als alle rondes voorbij zijn.

## Gevraagd

* Vraag het startaantal gelovers, de verspreidingsfactor, het factcheckpercentage, het aantal rondes en de virale grens.
* Gebruik variabelen zoals `gelovers`, `gedeeld`, `gecorrigeerd`, `factcheck` en `grens`.
* Bereken per ronde eerst hoeveel mensen het gerucht zouden geloven zonder factcheck.
* Bereken daarna hoeveel mensen door factchecks worden gecorrigeerd.
* Trek de gecorrigeerde mensen af van de groei.
* Print per ronde de tussenstand.
* Print op het einde of en wanneer het gerucht viraal ging.

#### Rekenregel

De factor komt eerst. Bij `gelovers = 10` en `factor = 3` krijg je `gedeeld = math.floor(10 * 3)`, dus 30 mensen zouden het gerucht geloven. Daarna remt de factcheck dat aantal af. Bij `factcheck = 25` bereken je `gecorrigeerd = math.floor(30 * 25 / 100)`, dus 7 mensen geloven het gerucht toch niet. Het nieuwe aantal gelovers is dan `30 - 7 = 23`.

#### Voorbeeld

Voor deze invoer:
```
4
3
0
5
100
```

moet je programma exact dit printen:
```
Ronde 1: 12 mensen geloven het gerucht.
Ronde 2: 36 mensen geloven het gerucht.
Ronde 3: 108 mensen geloven het gerucht.
Het gerucht gaat viraal na 3 rondes.
```
