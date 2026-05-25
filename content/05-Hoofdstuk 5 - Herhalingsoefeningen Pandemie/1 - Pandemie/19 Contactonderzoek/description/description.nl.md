## Gegeven

Bij contactonderzoek noteer je wie contact had met een besmette persoon. Niet elk contact is even belangrijk: een langer contact telt als risicocontact.

De invoer stopt pas wanneer de naam `stop` wordt ingevoerd.

## Gevraagd

* Vraag telkens een `naam`.
* Stop de lus wanneer de naam `stop` is.
* Vraag voor elke andere naam het aantal minuten contact.
* Tel alle contacten in `aantal_contacten`.
* Tel contacten vanaf 15 minuten als `risicocontacten`.
* Onthoud ook het langste contact met `langste_naam` en `langste_duur`.
* Als er meteen `stop` wordt ingevoerd, print je dat er geen risicocontact gevonden werd.

#### Rekenregel

Een contact vanaf 15 minuten telt als risicocontact. Voor het langste contact vergelijk je elke nieuwe `duur` met `langste_duur`. Is de nieuwe duur groter, dan vervang je ook `langste_naam`.

#### Voorbeeld

Voor deze invoer:
```
Ali
20
Bo
5
stop
```

moet je programma exact dit printen:
```
Er zijn 2 contacten genoteerd.
Risicocontacten: 1
Langste contact: Ali (20 minuten)
```
