## Gegeven

Een ziekenhuis heeft maar een beperkt aantal bedden.

Je bekijkt wat er gebeurt na 1 nieuwe opnamegolf. Je berekent ook de straal van een ronde triagezone.

## Gevraagd

* Vraag de capaciteit van het ziekenhuis.
* Vraag hoeveel bedden al bezet zijn.
* Vraag hoeveel nieuwe opnames erbij komen.
* Vraag de oppervlakte van de triagezone.
* Bereken hoeveel bedden daarna bezet zijn.
* Bereken de straal van de ronde triagezone.
* Print het aantal bezette bedden.
* Print de straal van de triagezone, afgerond op twee decimalen.
* Print of er code rood is.

#### Rekenregel

Gebruik:

```
bezet = bezet + opnames
```

Als `bezet` groter is dan de capaciteit, is het code rood.

Voor een ronde triagezone gebruik je:

```
straal = round(math.sqrt(oppervlakte / math.pi), 2)
```

Daarvoor heb je `import math`, `math.sqrt()` en `math.pi` nodig.

#### Voorbeeld

Voor deze invoer:
```
60
50
20
314.16
```

moet je programma exact dit printen:
```
Bezette bedden: 70
Straal triagezone: 10.0
Code rood.
```
