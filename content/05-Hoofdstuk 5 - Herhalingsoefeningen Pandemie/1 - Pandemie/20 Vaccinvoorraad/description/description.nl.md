## Gegeven

Een vaccinatiecentrum moet niet alleen weten hoeveel dosissen nodig zijn. Vaccins zitten in flacons, en flacons worden geleverd in dozen.

Je rekent dus in drie stappen: dosissen, flacons en dozen.

## Gevraagd

* Vraag het aantal personen, het aantal dosissen per persoon, het aantal dosissen per flacon en het aantal flacons per doos.
* Bereken het totaal aantal `dosissen`.
* Bereken met gehele deling en rest hoeveel `flacons` nodig zijn.
* Bereken hoeveel volle dozen en losse flacons dat zijn.
* Bereken hoeveel dozen besteld moeten worden als losse flacons ook een extra doos nodig maken.

#### Rekenregel

Eerst bereken je `dosissen = personen * dosissen_per_persoon`. Voor flacons rond je naar boven af. Dat kan met gehele deling: als er een rest is, heb je een extra flacon nodig. Voor dozen gebruik je `//` voor volle dozen en `%` voor losse flacons.

#### Voorbeeld

Voor deze invoer:
```
125
2
6
10
```

moet je programma exact dit printen:
```
Nodige dosissen: 250
Nodige flacons: 42
Volle dozen: 4
Losse flacons: 2
Te bestellen dozen: 5
```
