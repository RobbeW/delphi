## Gegeven

Een vaccinatiecampagne verlaagt het aantal personen dat nog vatbaar is.

In deze oefening loopt de campagne een vast aantal weken. Elke week worden evenveel mensen gevaccineerd.

## Gevraagd

* Vraag de grootte van de bevolking.
* Vraag hoeveel mensen per week gevaccineerd worden.
* Vraag hoeveel weken de campagne duurt.
* Bereken hoeveel mensen na die weken gevaccineerd zijn.
* Zorg ervoor dat het aantal gevaccineerden nooit groter wordt dan de bevolking.
* Tel ook hoeveel controlemomenten er zijn als er om de 2 weken controle is.
* Print hoeveel mensen gevaccineerd zijn, hoeveel mensen nog vatbaar zijn en hoeveel controles er zijn.

#### Rekenregel

Tel elke week het aantal vaccinaties erbij.

Als het aantal gevaccineerden groter wordt dan de bevolking, maak je het gelijk aan de bevolking.

Voor de controles gebruik je een `range()` met stapgrootte:

```
for week in range(2, weken + 1, 2):
```

#### Voorbeeld

Voor deze invoer:
```
1200
100
3
```

moet je programma exact dit printen:
```
Gevaccineerd: 300
Nog vatbaar: 900
Controles: 1
```
