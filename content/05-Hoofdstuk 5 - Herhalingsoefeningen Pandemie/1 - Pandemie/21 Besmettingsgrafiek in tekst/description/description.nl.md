## Gegeven

Een grafiek hoeft niet altijd met echte assen en kleuren te werken. In de console kun je een eenvoudige besmettingsgrafiek maken met sterretjes.

Elke ster stelt een vast aantal besmettingen voor. Zo oefen je tegelijk met groei en stringherhaling.

## Gevraagd

* Vraag het aantal weken, het startaantal besmettingen, de groeifactor en de schaalwaarde per ster.
* Gebruik variabelen zoals `besmettingen`, `factor`, `schaal` en `sterren`.
* Print per week het aantal besmettingen tussen haakjes.
* Print daarnaast een rij sterretjes die bij dat aantal hoort.
* Werk daarna het aantal besmettingen bij voor de volgende week.

#### Rekenregel

Het aantal sterretjes is `besmettingen // schaal`. Bij 40 besmettingen en schaal 10 print je dus 4 sterretjes. Als er wel besmettingen zijn maar de deling 0 sterretjes geeft, print je toch 1 sterretje. Voor de volgende week wordt `besmettingen = math.floor(besmettingen * factor)`.

#### Voorbeeld

Voor deze invoer:
```
3
20
2
10
```

moet je programma exact dit printen:
```
Week 1 (20): **
Week 2 (40): ****
Week 3 (80): ********
```
