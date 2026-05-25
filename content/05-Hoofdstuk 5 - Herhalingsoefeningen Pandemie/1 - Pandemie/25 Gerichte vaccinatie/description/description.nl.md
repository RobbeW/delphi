## Gegeven

Als vaccins schaars zijn, kan het slim zijn om eerst mensen met veel contacten te vaccineren. Zo bescherm je niet alleen die personen, maar verklein je ook veel mogelijke besmettingsroutes.

Je zoekt telkens de nog niet gevaccineerde persoon met de meeste contacten.

## Gevraagd

* Vraag het aantal personen en het aantal beschikbare vaccins.
* Vraag per persoon het aantal contacten.
* Gebruik een lijst zoals `contacten` en hou bij wie al gevaccineerd is.
* Kies per vaccin de persoon met de meeste overblijvende contacten.
* Print per vaccin wie gevaccineerd wordt.
* Tel alle beschermde contacten op en print dat totaal.

#### Rekenregel

Zoek telkens de grootste waarde in `contacten`. Na een vaccin tel je die waarde bij `beschermde_contacten` en zet je die plek in de lijst op `-1`, zodat dezelfde persoon niet opnieuw gekozen kan worden.

#### Voorbeeld

Voor deze invoer:
```
5
3
3
12
8
20
10
```

moet je programma exact dit printen:
```
Vaccin 1: persoon 4 met 20 contacten
Vaccin 2: persoon 2 met 12 contacten
Vaccin 3: persoon 5 met 10 contacten
Beschermde contacten: 42
```
