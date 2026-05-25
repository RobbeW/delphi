## Gegeven

Virussen blijven niet altijd hetzelfde. Een mutatie kan de `R0` lager maken, ongeveer gelijk houden of net verhogen. Daardoor verandert de groei tijdens de simulatie.

Je simuleert meerdere cycli. In elke cyclus bepaalt een willekeurig getal hoe de variant verandert.

## Gevraagd

* Vraag de startwaarde van `r0`, het startaantal besmettingen en het aantal cycli.
* Gebruik per cyclus `random.randint(1, 3)` om de mutatie te bepalen.
* Pas `r0` aan en rond de waarde af op twee decimalen.
* Bereken daarna het aantal `nieuwe_besmettingen` en het nieuwe `totaal`.
* Print per cyclus het type variant, de `R0`, de nieuwe besmettingen en het totaal.
* Print op het einde of de variant blijft groeien.

#### Rekenregel

Een mutatie met waarde 1 maakt `r0` 0.25 lager, maar nooit lager dan 0. Een mutatie met waarde 2 laat `r0` gelijk. Een mutatie met waarde 3 maakt `r0` 0.4 hoger. Rond `r0` daarna af op twee decimalen en bereken `nieuwe_besmettingen = math.floor(besmettingen * r0)`.

#### Voorbeeld

Voor deze invoer:
```
1.5
10
4
```

kan je programma bijvoorbeeld dit printen:
```
Cyclus 1: variant zwakker, R0 = 1.25, nieuwe besmettingen = 12, totaal = 22
Cyclus 2: variant stabiel, R0 = 1.25, nieuwe besmettingen = 15, totaal = 37
Cyclus 3: variant besmettelijker, R0 = 1.65, nieuwe besmettingen = 24, totaal = 61
Cyclus 4: variant stabiel, R0 = 1.65, nieuwe besmettingen = 39, totaal = 100
De variant blijft groeien.
```
