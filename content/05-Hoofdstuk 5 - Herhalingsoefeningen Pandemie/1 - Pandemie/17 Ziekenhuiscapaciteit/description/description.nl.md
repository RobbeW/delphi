## Gegeven

Een ziekenhuis raakt niet alleen overbelast door nieuwe opnames. Er vertrekken ook patienten omdat ze genezen. Daarom moet je per dag de bezette bedden bijwerken.

Code rood start op de eerste dag waarop de capaciteit overschreden wordt.

## Gevraagd

* Vraag de capaciteit, het startaantal bezette bedden en het aantal dagen.
* Vraag per dag het aantal nieuwe opnames en het aantal ontslagen patienten.
* Gebruik variabelen zoals `bezet`, `opnames`, `ontslagen` en `code_rood_dag`.
* Print per dag hoeveel bedden bezet zijn.
* Print op het einde de eerste code-rood-dag of dat er genoeg capaciteit bleef.

#### Rekenregel

Per dag wordt `bezet = bezet + opnames - ontslagen`. Controleer na die berekening of `bezet` groter is dan de capaciteit. De eerste dag waarop dat gebeurt, bewaar je als `code_rood_dag`.

#### Voorbeeld

Voor deze invoer:
```
60
50
2
20
5
10
8
```

moet je programma exact dit printen:
```
Dag 1: 65 bedden bezet
Dag 2: 67 bedden bezet
Code rood op dag 1.
```
