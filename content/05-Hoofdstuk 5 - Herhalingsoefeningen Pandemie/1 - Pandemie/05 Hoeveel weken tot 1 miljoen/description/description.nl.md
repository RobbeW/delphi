## Gegeven

Een uitbraak kan klein beginnen en toch enorm worden. Als besmettingen elke week vermenigvuldigen, wil je weten hoeveel weken nodig zijn voordat een grens wordt overschreden.

Deze oefening is bedoeld om een `while`-lus te gebruiken: je weet vooraf niet hoeveel herhalingen nodig zijn.

## Gevraagd

* Vraag het startaantal besmettingen, de groeifactor en de grens.
* Gebruik variabelen zoals `besmettingen`, `weken` en `grens`.
* Zolang het aantal besmettingen kleiner is dan de grens, vermenigvuldig je met de factor.
* Tel bij elke herhaling een week op.
* Print hoeveel weken nodig zijn en hoeveel besmettingen er dan zijn.

#### Rekenregel

Elke herhaling bereken je `volgende = math.floor(besmettingen * factor)`. Daarna wordt `besmettingen` gelijk aan `volgende`. De lus stopt pas zodra `besmettingen` minstens gelijk is aan de grens.

#### Voorbeeld

Voor deze invoer:
```
2
2
1000000
```

moet je programma exact dit printen:
```
Na 19 weken zijn er 1048576 besmettingen.
```
