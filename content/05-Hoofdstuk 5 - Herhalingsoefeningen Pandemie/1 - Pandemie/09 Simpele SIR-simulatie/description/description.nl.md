## Gegeven

Een SIR-model verdeelt een groep in drie delen:

* `vatbaar`: kan nog besmet raken
* `besmet`: is nu ziek
* `resistent`: is hersteld of beschermd

In deze oefening werk je meerdere rondes bij met een `for`-lus.

## Gevraagd

* Vraag het aantal vatbare, besmette en resistente personen.
* Vraag hoeveel rondes je simuleert.
* Vraag per ronde hoeveel nieuwe besmettingen er zijn.
* Vraag per ronde hoeveel besmette personen genezen.
* Werk de drie aantallen na elke ronde bij.
* Print de nieuwe toestand.

#### Rekenregel

Bij elke ronde:

```
vatbaar = vatbaar - nieuwe_besmettingen
besmet = besmet + nieuwe_besmettingen - genezen
resistent = resistent + genezen
```

De invoer is geldig: er genezen nooit meer personen dan er besmet zijn, en er raken nooit meer personen besmet dan er vatbaar zijn.

#### Voorbeeld

Voor deze invoer:
```
20
2
0
3
4
1
3
2
2
1
```

moet je programma exact dit printen:
```
Na 3 rondes: vatbaar=11, besmet=7, resistent=4
```
