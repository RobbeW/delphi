## Gegeven

Een epidemie stopt in dit model als de effectieve `R` kleiner is dan 1.

Vaccinatie verlaagt de effectieve `R`. Je onderzoekt meerdere vaccinatiescenario's met een `for`-lus.

## Gevraagd

* Vraag `r0`.
* Vraag hoeveel scenario's je onderzoekt.
* Vraag per scenario het vaccinatiepercentage.
* Bereken per scenario de effectieve `R`.
* Tel in hoeveel scenario's de epidemie stopt.
* Print dat aantal.

#### Rekenregel

Gebruik:

```
effectieve_r = r0 * (1 - vaccinatie / 100)
```

Rond de effectieve `R` per scenario af op twee decimalen. Een scenario stopt als de afgeronde effectieve `R` kleiner is dan 1.

#### Voorbeeld

Voor deze invoer:
```
2.5
4
80
60
20
90
```

moet je programma exact dit printen:
```
Scenario's waarin de epidemie stopt: 2
```
