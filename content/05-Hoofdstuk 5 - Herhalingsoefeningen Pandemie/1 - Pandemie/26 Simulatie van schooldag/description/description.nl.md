## Gegeven

Tijdens een schooldag kunnen besmettingen in een klas toenemen.

In deze oefening simuleer je 1 klas.

## Gevraagd

* Vraag de klasgrootte.
* Vraag het aantal besmette leerlingen bij de start.
* Vraag het aantal lessen.
* Bereken per les hoeveel nieuwe besmettingen erbij komen.
* Print na alle lessen hoeveel leerlingen besmet zijn.

#### Rekenregel

Per les kan elke besmette leerling 1 nieuwe leerling besmetten.

Gebruik:

```
nieuwe_besmettingen = min(vatbaar, besmet)
```

#### Voorbeeld

Voor deze invoer:
```
24
2
3
```

moet je programma exact dit printen:
```
Na 3 lessen zijn er 16 besmettingen.
```
