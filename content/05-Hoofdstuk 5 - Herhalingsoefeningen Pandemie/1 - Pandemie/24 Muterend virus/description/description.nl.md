## Gegeven

Een mutatie kan de `R0` van een virus veranderen.

In deze oefening bereken je de nieuwe `R0` na meerdere mutaties met een `for`-lus.

## Gevraagd

* Vraag de startwaarde van `R0`.
* Vraag hoeveel mutaties er zijn.
* Vraag per mutatie de verandering van `R0`.
* Bereken na elke mutatie de nieuwe `R0`.
* Print of de variant sterker, zwakker of stabiel is.

#### Rekenregel

Gebruik per mutatie:

```
nieuwe_r0 = round(nieuwe_r0 + verandering, 2)
```

Vergelijk daarna de nieuwe waarde met de oude waarde.

#### Voorbeeld

Voor deze invoer:
```
1.5
3
0.4
-0.1
0.25
```

moet je programma exact dit printen:
```
Nieuwe R0: 2.05
De variant wordt sterker.
```
