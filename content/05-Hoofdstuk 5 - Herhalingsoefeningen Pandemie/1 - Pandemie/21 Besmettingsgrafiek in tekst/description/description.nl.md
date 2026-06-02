## Gegeven

In de console kun je een eenvoudige grafiek maken met sterretjes.

Elke ster stelt een vast aantal besmettingen voor.

## Gevraagd

* Vraag het aantal weken.
* Vraag hoeveel besmettingen 1 ster voorstelt.
* Vraag per week het aantal besmettingen.
* Print per week een rij sterretjes.
* Als er nog een rest is, voeg je een `+` toe.

#### Rekenregel

Het aantal sterretjes is:

```
besmettingen // schaal
```

De rest bereken je met:

```
besmettingen % schaal
```

Als er besmettingen zijn maar het aantal volledige sterretjes 0 is, print je toch 1 ster. Als er minstens 1 volledige ster is en er blijft een rest over, voeg je een `+` toe.

#### Voorbeeld

Voor deze invoer:
```
3
10
20
35
80
```

moet je programma exact dit printen:
```
Week 1: **
Week 2: ***+
Week 3: ********
```
