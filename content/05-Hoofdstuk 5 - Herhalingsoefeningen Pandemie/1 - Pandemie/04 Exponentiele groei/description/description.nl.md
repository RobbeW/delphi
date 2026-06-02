## Gegeven

Bij exponentiele groei wordt een besmettingsgroep elke week met dezelfde factor groter.

In deze oefening simuleer je een vast aantal weken. Je hoeft niet vroeger te stoppen.

## Gevraagd

* Vraag het startaantal besmettingen.
* Vraag de groeifactor.
* Vraag het aantal weken.
* Bereken per week het aantal besmettingen met een macht.
* Print per week het nieuwe totaal.

#### Rekenregel

Bewaar eerst het startaantal. Gebruik daarna per week:

```
besmettingen = math.floor(start_besmettingen * (factor ** week))
```

Met `**` bereken je een macht. Met `math.floor()` rond je naar beneden af.

#### Voorbeeld

Voor deze invoer:
```
2
2
5
```

moet je programma exact dit printen:
```
Week 1: 4 besmettingen
Week 2: 8 besmettingen
Week 3: 16 besmettingen
Week 4: 32 besmettingen
Week 5: 64 besmettingen
```
