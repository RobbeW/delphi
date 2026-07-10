## Gegeven

Een vaccinatiecentrum wil weten of er genoeg dosissen op voorraad zijn.

Elke persoon heeft evenveel dosissen nodig. Je krijgt meerdere groepen personen.

## Gevraagd

* Vraag het aantal groepen.
* Vraag het aantal dosissen per persoon.
* Vraag hoeveel dosissen er op voorraad zijn.
* Vraag per groep hoeveel personen erin zitten.
* Bereken met een `for`-lus hoeveel dosissen in totaal nodig zijn.
* Print het aantal nodige dosissen.
* Print of er genoeg dosissen zijn of hoeveel tekort er is.

#### Rekenregel

Tel per groep dit aantal bij het totaal:

```
nodig += personen * dosissen_per_persoon
```

Als de voorraad kleiner is dan `nodig`, is het tekort `nodig - voorraad`.

#### Voorbeeld

Voor deze invoer:
```
3
2
300
50
75
25
```

moet je programma exact dit printen:
```
Nodige dosissen: 300
Er zijn genoeg dosissen.
```
