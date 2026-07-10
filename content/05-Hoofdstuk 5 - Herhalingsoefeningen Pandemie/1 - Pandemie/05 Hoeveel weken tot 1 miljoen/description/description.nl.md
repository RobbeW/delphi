## Gegeven

Een uitbraak kan klein beginnen en toch groot worden. Je wil weten hoeveel weken nodig zijn om minstens 1 miljoen besmettingen te bereiken.

Deze oefening gebruikt een `while`-lus: je weet vooraf niet hoeveel weken nodig zijn.

## Gevraagd

* Vraag het startaantal besmettingen.
* Vraag de groeifactor. Die is groter dan 1.
* Gebruik als grens `1000000`.
* Zolang het aantal besmettingen kleiner is dan de grens, vermenigvuldig je met de groeifactor.
* Tel bij elke herhaling een week op.
* Print hoeveel weken nodig zijn en hoeveel besmettingen er dan zijn.

#### Rekenregel

Gebruik in de lus:

```
besmettingen = math.floor(besmettingen * factor)
```

#### Voorbeeld

Voor deze invoer:
```
2
2
```

moet je programma exact dit printen:
```
Na 19 weken zijn er 1048576 besmettingen.
```
