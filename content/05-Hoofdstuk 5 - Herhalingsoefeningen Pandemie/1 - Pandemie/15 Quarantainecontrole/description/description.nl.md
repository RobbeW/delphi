## Gegeven

Een quarantainebeslissing hangt niet af van een enkel gegeven. Symptomen, een positieve test, een risicocontact en vaccinatiestatus spelen samen een rol.

Voor elke persoon krijg je antwoorden met `ja` of `nee`.

## Gevraagd

* Vraag hoeveel personen je controleert.
* Vraag per persoon of die symptomen heeft, positief testte, een risicocontact had en gevaccineerd is.
* Gebruik booleaanse variabelen zoals `symptomen`, `positief`, `risicocontact` en `gevaccineerd`.
* Plaats iemand altijd in quarantaine bij een positieve test.
* Zonder positieve test plaats je iemand alleen in quarantaine bij symptomen, een risicocontact en geen vaccinatie.
* Print per persoon de beslissing en daarna het totaal.

#### Rekenregel

Een persoon moet in quarantaine bij een positieve test. Zonder positieve test moet die alleen in quarantaine als er tegelijk symptomen, een risicocontact en geen vaccinatie zijn. In Python kun je dat denken als `positief or (symptomen and risicocontact and not gevaccineerd)`.

#### Voorbeeld

Voor deze invoer:
```
1
ja
nee
ja
nee
```

moet je programma exact dit printen:
```
Persoon 1: quarantaine
Totaal in quarantaine: 1
```
