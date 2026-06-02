## Gegeven

De gewone `R0` vertelt hoeveel mensen een besmet persoon gemiddeld besmet zonder bescherming.

Als een deel van de bevolking gevaccineerd is, wordt de verspreiding kleiner. Daarom berekenen we een effectieve `R`.

## Gevraagd

* Vraag `r0`.
* Vraag het vaccinatiepercentage.
* Bereken de effectieve `R`.
* Print de effectieve `R` met `round(..., 2)`.
* Print of de epidemie groeit, krimpt of stabiel blijft.

#### Rekenregel

Gebruik:

```
effectieve_r = r0 * (1 - vaccinatie / 100)
```

Daarna:

* groter dan 1: de epidemie groeit
* kleiner dan 1: de epidemie krimpt
* gelijk aan 1: de epidemie blijft stabiel

#### Voorbeeld

Voor deze invoer:
```
2.4
40
```

moet je programma exact dit printen:
```
Effectieve R: 1.44
De epidemie groeit.
```
