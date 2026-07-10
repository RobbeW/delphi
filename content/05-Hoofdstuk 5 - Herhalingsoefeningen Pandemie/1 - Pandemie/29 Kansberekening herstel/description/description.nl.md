## Gegeven

Een herstelkans kan je gebruiken om te berekenen hoeveel zieken ongeveer genezen.

In deze oefening bereken je het verwachte aantal genezingen voor meerdere groepen met een `for`-lus.

## Gevraagd

* Vraag hoeveel groepen zieken er zijn.
* Vraag per groep het aantal zieken.
* Vraag per groep de herstelkans in procent.
* Bereken per groep hoeveel mensen naar verwachting genezen.
* Tel alle genezen personen op.
* Tel ook alle personen op die ziek blijven.
* Print beide totalen.

#### Rekenregel

Gebruik:

```
genezen = math.floor(ziek * kans / 100)
```

Daarna:

```
nog_ziek = ziek - genezen
```

#### Voorbeeld

Voor deze invoer:
```
3
10
30
15
50
8
10
```

moet je programma exact dit printen:
```
Genezen: 10
Nog ziek: 23
```
