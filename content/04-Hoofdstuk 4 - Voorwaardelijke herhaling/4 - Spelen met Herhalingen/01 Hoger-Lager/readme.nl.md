## Opgave

Schrijf een programma dat een willekeurig getal neemt tussen 1 en 1 000. Het programma vraagt de gebruiker om het getal te raden.

Na iedere gok van de gebruiker verschijnt één van de volgende boodschappen:

- `"Het getal is lager dan ..."` indien de gebruiker lager moet gokken.
- `"Het getal is hoger dan ..."` indien de gebruiker hoger moet gokken.
- `"Je hebt ... meteen geraden!"` indien de gebruiker het getal in één poging raadt.
- `"Je hebt ... geraden in ... pogingen!"` indien de gebruiker het getal correct raadt na meer dan één poging.


#### Voorbeeld

Stel dat het willekeurige getal `614` is. Indien de gebruiker achtereenvolgens de getallen `500`, `750`, `600` en `614` ingeeft, dan verschijnt er:

```
Het getal is hoger dan 500
Het getal is lager dan 750
Het getal is hoger dan 600
Je hebt 614 geraden in 4 pogingen!
```

Indien de gebruiker het getal meteen juist raadt, bijvoorbeeld 614, dan verschijnt er:
```
Je hebt 614 meteen geraden!

```

{: .callout.callout-info}
> #### Tips
> - Gebruik `random.randint(1, 1000)` om een willekeurig getal tussen 1 en 1 000 door de computer te laten genereren.
> - Geef het *te raden getal* weer terwijl je het programma uittest.
