## Gegeven

Niet iedereen loopt hetzelfde risico op ernstige ziekte. Leeftijd, vaccinatiestatus en chronische aandoeningen kunnen samen een risicoscore vormen.

Je beoordeelt meerdere personen en telt hoeveel personen in de hoge risicogroep vallen.

## Gevraagd

* Vraag hoeveel personen je onderzoekt.
* Vraag per persoon de leeftijd, of die gevaccineerd is en of die een chronische aandoening heeft.
* Bouw per persoon een `score` op met `if`, `elif` en `else`.
* Print per persoon de score en de risicocategorie.
* Tel hoeveel personen `hoog` risico hebben en print dat op het einde.

#### Rekenregel

De score wordt opgebouwd uit meerdere beslissingen. Vanaf 65 jaar krijgt iemand 2 punten, vanaf 45 jaar 1 punt. Niet gevaccineerd zijn geeft 1 extra punt en een chronische aandoening geeft 2 extra punten. Vanaf score 4 is het risico `hoog`, vanaf score 2 is het `matig`, anders is het `laag`.

#### Voorbeeld

Voor deze invoer:
```
1
70
nee
ja
```

moet je programma exact dit printen:
```
Persoon 1: score 5, risico hoog
Aantal hoog risico: 1
```
