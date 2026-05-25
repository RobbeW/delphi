## Gegeven

De gewone `R0` vertelt hoeveel mensen een besmet persoon gemiddeld besmet zonder bescherming. In het echt zijn er ook gevaccineerden en maatregelen, zoals maskers, die de verspreiding afremmen.

Daarom berekenen we een effectieve `R`: die toont of een epidemie in deze situatie groeit of krimpt.

## Gevraagd

* Vraag `r0`, het vaccinatiepercentage, het maskerpercentage, het startaantal besmettingen en het aantal cycli.
* Bereken de effectieve `R` met variabelen zoals `vaccinatie_deel`, `masker_deel` en `effectieve_r`.
* Print de effectieve `R`, afgerond op twee decimalen.
* Print of de epidemie groeit, stabiel blijft of krimpt.
* Simuleer daarna per cyclus hoeveel nieuwe besmettingen ontstaan.

#### Rekenregel

De effectieve R bereken je met `effectieve_r = r0 * (1 - vaccinatie / 100) * (1 - maskers / 100)`. Bij `r0 = 2.4`, `vaccinatie = 40` en `maskers = 20` wordt dat `2.4 * 0.6 * 0.8 = 1.152`, afgerond `1.15`. Per cyclus wordt het aantal nieuwe besmettingen `math.floor(besmettingen * effectieve_r)`.

#### Voorbeeld

Voor deze invoer:
```
2.4
40
20
15
4
```

moet je programma exact dit printen:
```
Effectieve R: 1.15
De epidemie groeit.
Cyclus 1: 17 nieuwe besmettingen
Cyclus 2: 19 nieuwe besmettingen
Cyclus 3: 21 nieuwe besmettingen
Cyclus 4: 24 nieuwe besmettingen
```
