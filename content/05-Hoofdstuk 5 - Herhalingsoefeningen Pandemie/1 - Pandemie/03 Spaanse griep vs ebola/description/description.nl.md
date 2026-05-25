## Gegeven

Niet elke ziekte is op dezelfde manier gevaarlijk. Sommige ziektes verspreiden zich zeer breed, andere ziektes zijn minder wijd verspreid maar wel dodelijker voor wie besmet raakt.

Je vergelijkt twee ziektes door voor beide een verwacht aantal overlijdens te berekenen.

## Gevraagd

* Vraag het aantal besmettingen en het sterftepercentage voor Spaanse griep.
* Vraag daarna hetzelfde voor ebola.
* Bereken de verwachte overlijdens met variabelen zoals `overlijdens_spaanse_griep` en `overlijdens_ebola`.
* Print beide verwachte aantallen overlijdens.
* Vergelijk de aantallen en print welke ziekte in dit scenario de grootste dodentol heeft.

#### Rekenregel

Een sterftepercentage is een deel van 100. Bij 2.5% bereken je dus `besmettingen * 2.5 / 100`. Rond het aantal verwachte overlijdens naar beneden af met `math.floor()`.

#### Voorbeeld

Voor deze invoer:
```
500000
2.5
1000
50
```

moet je programma exact dit printen:
```
Spaanse griep: 12500 verwachte overlijdens
Ebola: 500 verwachte overlijdens
Grootste dodentol: Spaanse griep.
```
