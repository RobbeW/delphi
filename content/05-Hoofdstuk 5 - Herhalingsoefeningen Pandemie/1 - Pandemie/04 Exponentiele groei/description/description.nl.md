## Gegeven

Bij exponentiele groei wordt een besmettingsgroep elke ronde met dezelfde factor groter. Dat lijkt in het begin onschuldig, maar na enkele weken kan de stijging plots heel snel gaan.

In deze oefening werk je week per week en hou je zelf het huidige aantal besmettingen bij.

## Gevraagd

* Vraag het startaantal besmettingen, de groeifactor, het aantal weken en een alarmgrens.
* Gebruik variabelen zoals `besmettingen`, `factor` en `week`.
* Vermenigvuldig het aantal besmettingen elke week met de factor.
* Print per week het nieuwe totaal.
* Stop vroeger als de alarmgrens bereikt of overschreden wordt.
* Als de alarmgrens al bij de start bereikt is, print je meteen `De grens is al bereikt.`

#### Rekenregel

In elke week wordt het nieuwe aantal `math.floor(besmettingen * factor)`. Met startwaarde 2 en factor 2 krijg je dus 4, daarna 8, daarna 16. Als het nieuwe aantal boven de grens gaat, zet je het gelijk aan de grens en meld je in welke week de grens bereikt wordt.

#### Voorbeeld

Voor deze invoer:
```
2
2
5
1000
```

moet je programma exact dit printen:
```
Week 1: 4 besmettingen
Week 2: 8 besmettingen
Week 3: 16 besmettingen
Week 4: 32 besmettingen
Week 5: 64 besmettingen
```
