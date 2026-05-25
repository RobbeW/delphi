## Gegeven

In sociale netwerken lijkt het vaak alsof je vrienden populairder zijn dan jij. Dat komt doordat mensen met veel contacten in veel vriendengroepen tegelijk opduiken.

Je onderzoekt een kleine groep personen en vergelijkt hun aantal vrienden.

## Gevraagd

* Vraag hoeveel personen je onderzoekt.
* Vraag per persoon het aantal vrienden.
* Bereken het gemiddelde met variabelen zoals `totaal` en `gemiddelde`.
* Zoek de populairste persoon met `max_vrienden` en `populairste_persoon`.
* Tel hoeveel personen minder vrienden hebben dan het gemiddelde.
* Print het gemiddelde, de populairste persoon en het aantal personen onder het gemiddelde.

#### Rekenregel

Het gemiddelde is `totaal / aantal_personen`, afgerond op twee decimalen. Daarna vergelijk je elke persoon opnieuw met dat gemiddelde om te tellen wie eronder zit.

#### Voorbeeld

Voor deze invoer:
```
4
3
8
2
5
```

moet je programma exact dit printen:
```
Gemiddeld aantal vrienden: 4.5
Populairste persoon: 2 met 8 vrienden.
Aantal personen onder het gemiddelde: 2
```
