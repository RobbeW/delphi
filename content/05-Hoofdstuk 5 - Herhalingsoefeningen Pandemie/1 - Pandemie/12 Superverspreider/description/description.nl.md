## Gegeven

Bij sommige uitbraken veroorzaakt een klein aantal personen uitzonderlijk veel besmettingen. Zulke personen noemen we superverspreiders.

In deze simulatie krijgt elke besmette persoon willekeurig een score van 1 tot en met 10. Alleen wie hoog genoeg scoort, wordt een superverspreider.

## Gevraagd

* Vraag het aantal besmette personen en het aantal gewone besmettingen per persoon.
* Gebruik voor elke persoon `random.randint(1, 10)`.
* Als de score minstens 9 is, telt die persoon als `superverspreider` en veroorzaakt die 25 nieuwe besmettingen.
* Andere personen veroorzaken alleen het gewone aantal nieuwe besmettingen.
* Print het aantal superverspreiders en het totaal aantal nieuwe besmettingen.

#### Rekenregel

Elke persoon krijgt een score. Bij `score >= 9` tel je 25 nieuwe besmettingen. Anders tel je alleen het gewone aantal besmettingen. Tel alle nieuwe besmettingen samen in `nieuwe_besmettingen`.

#### Voorbeeld

Voor deze invoer:
```
8
2
```

kan je programma bijvoorbeeld dit printen:
```
Superverspreiders: 2
Nieuwe besmettingen: 62
```
