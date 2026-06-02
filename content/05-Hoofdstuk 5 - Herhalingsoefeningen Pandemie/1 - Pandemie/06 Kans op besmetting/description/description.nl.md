## Gegeven

Niet elk contact leidt tot een besmetting. Met een besmettingskans kan je berekenen hoeveel besmettingen je ongeveer verwacht.

In deze oefening gebruiken we geen willekeur. Je berekent alleen het verwachte aantal besmettingen.

## Gevraagd

* Vraag het aantal contacten.
* Vraag de besmettingskans in procent.
* Bereken hoeveel contacten je verwacht te besmetten.
* Print het verwachte aantal besmette en niet-besmette contacten.
* Bereken vanaf hoeveel contacten je minstens 1 besmetting verwacht.

#### Rekenregel

Gebruik:

```
besmet = math.floor(contacten * kans / 100)
```

Daarna is:

```
niet_besmet = contacten - besmet
```

Als `kans <= 0` of `contacten <= 0`, dan is het minimum `0`.

Anders gebruik je:

```
minimum_contacten = math.ceil(100 / kans)
```

Met `math.ceil()` rond je naar boven af.

#### Voorbeeld

Voor deze invoer:
```
10
30
```

moet je programma exact dit printen:
```
Verwacht besmet: 3
Verwacht niet besmet: 7
Minstens 1 verwacht vanaf: 4 contacten
```
