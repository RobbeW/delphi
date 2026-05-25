## Gegeven

Een vaccinatiecampagne verlaagt het aantal vatbare personen in een bevolking. Elke week worden er vaccins gezet, maar het doel is niet altijd om iedereen te bereiken.

Je berekent week per week hoeveel mensen al gevaccineerd zijn en hoeveel mensen daarna nog vatbaar blijven.

## Gevraagd

* Vraag de grootte van de bevolking, het aantal vaccinaties per week en het doelpercentage.
* Bereken met variabelen zoals `doel`, `gevaccineerd` en `week` hoeveel mensen minstens gevaccineerd moeten worden.
* Verhoog het aantal gevaccineerden week per week.
* Print na elke week hoeveel mensen gevaccineerd zijn.
* Print op het einde hoeveel mensen nog vatbaar zijn.

#### Rekenregel

Het vaccinatiedoel is `math.ceil(populatie * doelpercentage / 100)`. Je rondt dus naar boven af, want bij 840.2 personen moet je 841 mensen vaccineren om het doel echt te halen.

#### Voorbeeld

Voor deze invoer:
```
1200
100
70
```

moet je programma exact dit printen:
```
Week 1: 100 mensen gevaccineerd
Week 2: 200 mensen gevaccineerd
Week 3: 300 mensen gevaccineerd
Week 4: 400 mensen gevaccineerd
Week 5: 500 mensen gevaccineerd
Week 6: 600 mensen gevaccineerd
Week 7: 700 mensen gevaccineerd
Week 8: 800 mensen gevaccineerd
Week 9: 900 mensen gevaccineerd
Nog vatbaar: 300
```
