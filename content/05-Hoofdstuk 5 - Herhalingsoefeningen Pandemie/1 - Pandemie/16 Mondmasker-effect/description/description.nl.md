## Gegeven

Mondmaskers voorkomen niet elke besmetting, maar ze kunnen het aantal besmettingen wel verlagen. Per dag vergelijk je het verwachte aantal besmettingen met het percentage dat vermeden wordt.

Je telt de vermeden besmettingen over meerdere dagen op.

## Gevraagd

* Vraag het aantal dagen en het beschermingspercentage van de mondmaskers.
* Vraag daarna per dag het verwachte aantal besmettingen zonder mondmaskers.
* Bereken per dag het aantal `vermeden` besmettingen.
* Gebruik `round()` om het dagresultaat op twee decimalen af te ronden.
* Tel alles op in `totaal_vermeden` en print dat op het einde.

#### Rekenregel

Het percentage werkt als een deel van 100: `vermeden = round(verwacht * effect / 100, 2)`. Bij 120 verwachte besmettingen en 25% effect vermijd je dus `120 * 25 / 100 = 30.0` besmettingen.

#### Voorbeeld

Voor deze invoer:
```
3
25
120
80
60
```

moet je programma exact dit printen:
```
Dag 1: 30.0 besmettingen vermeden
Dag 2: 20.0 besmettingen vermeden
Dag 3: 15.0 besmettingen vermeden
Totaal vermeden: 65.0
```
