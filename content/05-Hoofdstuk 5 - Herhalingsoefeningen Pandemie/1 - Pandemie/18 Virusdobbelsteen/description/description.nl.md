## Gegeven

Soms bouw je een eenvoudige simulatie zonder ingewikkelde kansformules. Een dobbelsteen kan dan bepalen hoeveel nieuwe besmettingen er per beurt bijkomen.

De simulatie stopt wanneer een besmettingsgrens bereikt wordt of wanneer het maximaal aantal beurten voorbij is.

## Gevraagd

* Vraag de besmettingsgrens en het maximaal aantal beurten.
* Gooi per beurt met `random.randint(1, 6)`.
* Tel de worpen op in `totaal`.
* Print per beurt de worp en de nieuwe tussenstand.
* Print daarna of de grens bereikt werd of hoeveel besmettingen er na alle beurten zijn.

#### Rekenregel

Elke dobbelsteenworp is het aantal nieuwe besmettingen van die beurt. Je werkt dus telkens bij met `totaal = totaal + worp`. Stop zodra `totaal` minstens gelijk is aan de grens.

#### Voorbeeld

Voor deze invoer:
```
30
8
```

kan je programma bijvoorbeeld dit printen:
```
Beurt 1: +4 besmettingen, totaal 4
Beurt 2: +3 besmettingen, totaal 7
Beurt 3: +2 besmettingen, totaal 9
Beurt 4: +1 besmettingen, totaal 10
Beurt 5: +6 besmettingen, totaal 16
Beurt 6: +5 besmettingen, totaal 21
Beurt 7: +4 besmettingen, totaal 25
Beurt 8: +3 besmettingen, totaal 28
Na 8 beurten zijn er 28 besmettingen.
```
