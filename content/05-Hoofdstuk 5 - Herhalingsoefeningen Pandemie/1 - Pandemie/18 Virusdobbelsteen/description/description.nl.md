## Gegeven

Een dobbelsteenmodel kan per beurt een ander aantal besmettingen geven.

In deze oefening simuleer je de worpen zelf met de module `random`.

## Gevraagd

* Vraag het aantal beurten.
* Simuleer per beurt een worp met `random.randint(1, 6)`.
* Bereken het totaal aantal besmettingen.
* Print het resultaat.

#### Rekenregel

Start met:

```
totaal = 0
```

Tel daarna in een lus elke willekeurige worp bij `totaal`.

#### Voorbeeld

Voor deze invoer:
```
8
```

kan je programma bijvoorbeeld dit printen:
```
Na 8 beurten zijn er 27 besmettingen.
```

{: .callout.callout-info}
>#### Tips
>* Zet bovenaan `import random`.
>* Gebruik in de lus `random.randint(1, 6)` om een worp te maken.
