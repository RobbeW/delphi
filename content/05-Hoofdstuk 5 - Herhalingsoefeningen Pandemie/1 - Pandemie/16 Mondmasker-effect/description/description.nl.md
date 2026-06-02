## Gegeven

Mondmaskers kunnen een deel van de besmettingen vermijden.

In deze oefening bereken je dat voor meerdere dagen met een `for`-lus.

## Gevraagd

* Vraag hoeveel dagen je onderzoekt.
* Vraag per dag het verwachte aantal besmettingen zonder mondmaskers.
* Vraag per dag het beschermingspercentage.
* Bereken per dag hoeveel besmettingen vermeden worden.
* Tel alle vermeden besmettingen op.
* Tel ook alle overblijvende besmettingen met mondmaskers op.
* Print beide totalen.

#### Rekenregel

Gebruik:

```
vermeden = math.floor(verwacht * effect / 100)
```

Daarna is:

```
met_maskers = verwacht - vermeden
```

#### Voorbeeld

Voor deze invoer:
```
3
120
25
80
50
33
30
```

moet je programma exact dit printen:
```
Totaal vermeden besmettingen: 79
Totaal met mondmaskers: 154
```
