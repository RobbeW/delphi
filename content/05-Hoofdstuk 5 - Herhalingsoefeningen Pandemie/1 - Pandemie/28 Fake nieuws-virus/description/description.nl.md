## Gegeven

Factchecks kunnen ervoor zorgen dat minder mensen fake nieuws blijven geloven. Een bericht met veel uitroeptekens kan extra opvallend zijn.

In deze oefening tel je eerst de uitroeptekens in een bericht. Daarna verwerk je factcheckpercentages tot de invoer `"stop"` is.

## Gevraagd

* Vraag het bericht.
* Vraag hoeveel mensen het fake nieuws geloven.
* Overloop het bericht letter per letter en tel de uitroeptekens.
* Vraag telkens een factcheckpercentage of `"stop"`.
* Bereken per ronde hoeveel mensen gecorrigeerd worden.
* Werk na elke ronde bij hoeveel mensen nog blijven geloven.
* Print het aantal alarmtekens, het aantal gecorrigeerde mensen en hoeveel mensen blijven geloven.

#### Rekenregel

Gebruik:

```
gecorrigeerd = math.floor(gelovers * factcheck / 100)
```

Daarna:

```
blijft_geloven = gelovers - gecorrigeerd
```

Voor de factchecks gebruik je een sentinel-lus:

```
while antwoord != "stop":
```

#### Voorbeeld

Voor deze invoer:
```
PAS OP!!
100
25
50
11
stop
```

moet je programma exact dit printen:
```
Alarmtekens: 2
Gecorrigeerd: 66
Blijft geloven: 34
```
