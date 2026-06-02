## Gegeven

Bij contactonderzoek telt een contact vanaf 15 minuten als risicocontact, behalve als er bescherming was.

In deze oefening krijg je een vast aantal contacten.

## Gevraagd

* Vraag hoeveel contacten je controleert.
* Vraag per contact het aantal minuten.
* Vraag per contact of er bescherming was: `ja` of `nee`.
* Tel hoeveel contacten minstens 15 minuten duurden en niet beschermd waren.
* Print het aantal risicocontacten.

#### Rekenregel

Een contact is een risicocontact als:

```
minuten >= 15 and not is_beschermd
```

#### Voorbeeld

Voor deze invoer:
```
2
20
nee
5
nee
```

moet je programma exact dit printen:
```
Risicocontacten: 1
```
