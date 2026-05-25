## Gegeven

Een nieuw virus duikt op in verschillende wijken. De eerste cijfers zijn nog klein, maar de onderzoekers willen meteen weten hoeveel besmettingen er in totaal zijn. Ook willen ze weten welke wijk de meeste besmettingen telt.

Een uitbraak onder de 20 besmettingen noemen we voorlopig rustig. Vanaf 20 besmettingen moet de situatie opgevolgd worden.

## Gevraagd

* Vraag eerst het aantal wijken en bewaar dit bijvoorbeeld in `aantal_wijken`.
* Vraag daarna per wijk het aantal besmette personen.
* Tel alle besmettingen op in `totaal`.
* Onthoud welke wijk het zwaarst getroffen is met variabelen zoals `max_besmettingen` en `max_wijk`.
* Print het totaal, de zwaarst getroffen wijk en de status.

#### Rekenregel

Bij elke wijk tel je de besmettingen op bij `totaal`. Tegelijk vergelijk je het nieuwe aantal met `max_besmettingen`. Is de huidige wijk groter, dan bewaar je die wijk als `max_wijk`.

#### Voorbeeld

Voor deze invoer:
```
3
12
4
19
```

moet je programma exact dit printen:
```
Totaal besmet: 35
Zwaarst getroffen wijk: 3 met 19 besmettingen.
Status: opvolgen.
```
