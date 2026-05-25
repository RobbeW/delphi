## Gegeven

Naast besmettingen wil je ook herstel kunnen simuleren. Elke zieke persoon heeft per dag een kans om te genezen.

Voor elke zieke persoon trek je een willekeurig getal. Wie binnen de herstelkans valt, geneest en telt de volgende dag niet meer mee als ziek.

## Gevraagd

* Vraag het startaantal zieken, de herstelkans in procent en het aantal dagen.
* Gebruik per zieke persoon `random.randint(1, 100)`.
* Tel per dag hoeveel personen `genezen`.
* Verminder het aantal `ziek` met het aantal genezen personen.
* Print per dag de genezingen en het aantal zieken.
* Print op het einde het totaal aantal genezen personen.

#### Rekenregel

Voor elke zieke persoon trek je een getal van 1 tot en met 100. Als `worp <= herstelkans`, dan geneest die persoon. Na de dag wordt `ziek = ziek - genezen`.

#### Voorbeeld

Voor deze invoer:
```
10
30
5
```

kan je programma bijvoorbeeld dit printen:
```
Dag 1: 3 genezen, 7 ziek
Dag 2: 1 genezen, 6 ziek
Dag 3: 2 genezen, 4 ziek
Dag 4: 2 genezen, 2 ziek
Dag 5: 0 genezen, 2 ziek
Totaal genezen: 8
```
