## Gegeven

Een besmettingsratio zegt hoeveel nieuwe personen elke besmette persoon gemiddeld besmet.

In deze oefening gebruiken we een eenvoudige versie: `r0` is een geheel getal. Als er 10 besmette personen zijn en `r0` is 2, dan komen er 20 nieuwe besmettingen bij.

## Gevraagd

* Vraag `r0`, het startaantal besmettingen en het aantal cycli.
* Bereken per cyclus hoeveel nieuwe besmettingen erbij komen.
* Tel de nieuwe besmettingen bij het totaal.
* Print na elke cyclus het totaal aantal besmettingen.

#### Rekenregel

Per cyclus:

1. `nieuwe_besmettingen = besmettingen * r0`
2. `besmettingen = besmettingen + nieuwe_besmettingen`

#### Voorbeeld

Voor deze invoer:
```
2
10
3
```

moet je programma exact dit printen:
```
Na 1 cycli zijn er 30 besmettingen.
Na 2 cycli zijn er 90 besmettingen.
Na 3 cycli zijn er 270 besmettingen.
```
