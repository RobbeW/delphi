## Gegeven

Een virus verspreidt zich in besmettingscycli. Elke besmette persoon kan gemiddeld een aantal nieuwe personen besmetten. Dat gemiddelde noemen we de besmettingsratio of `R0`.

In deze oefening groeit het aantal besmettingen per cyclus. Je stopt zodra de simulatie het maximum aantal besmettingen bereikt of overschrijdt.

## Gevraagd

* Vraag `r0`, het startaantal besmettingen en het maximum aantal besmettingen.
* Bereken per cyclus hoeveel nieuwe besmettingen erbij komen.
* Gebruik variabelen zoals `besmet`, `cyclus` en `nieuwe_besmettingen` om de groei bij te houden.
* Print na elke cyclus het totaal aantal besmettingen.
* Stop wanneer het totaal minstens gelijk is aan het maximum.

#### Rekenregel

Per cyclus bereken je eerst `nieuwe_besmettingen = math.floor(besmet * r0)`. Daarna tel je die nieuwe besmettingen bij het bestaande totaal. Als het totaal daardoor boven het maximum zou gaan, gebruik je alleen het aantal dat nog nodig is om precies aan het maximum te komen.

#### Voorbeeld

Voor deze invoer:
```
2.4
20
1200
```

moet je programma exact dit printen:
```
Na 1 cycli zijn er 68 besmettingen.
Na 2 cycli zijn er 231 besmettingen.
Na 3 cycli zijn er 785 besmettingen.
Na 4 cycli zijn er 1200 besmettingen.
```
