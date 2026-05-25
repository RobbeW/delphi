## Gegeven

In een klassiek SIR-model blijven genezen personen resistent. Bij sommige ziektes is dat te eenvoudig: een deel van de resistente groep kan later opnieuw besmet raken.

Je simuleert per ronde of elke resistente persoon opnieuw besmet raakt.

## Gevraagd

* Vraag het aantal resistente personen, het aantal rondes en de kans op herinfectie in procent.
* Gebruik per resistente persoon `random.randint(1, 100)`.
* Tel per ronde het aantal `herinfecties`.
* Verminder `resistent` met het aantal herinfecties.
* Print per ronde de herinfecties en print op het einde het totaal.

#### Rekenregel

Voor elke resistente persoon trek je een getal van 1 tot en met 100. Als `worp <= kans`, dan wordt die persoon opnieuw ziek en daalt het aantal resistente personen met 1.

#### Voorbeeld

Voor deze invoer:
```
12
4
25
```

kan je programma bijvoorbeeld dit printen:
```
Ronde 1: 2 herinfecties, 10 resistent
Ronde 2: 3 herinfecties, 7 resistent
Ronde 3: 2 herinfecties, 5 resistent
Ronde 4: 2 herinfecties, 3 resistent
Totaal herinfecties: 9
```
