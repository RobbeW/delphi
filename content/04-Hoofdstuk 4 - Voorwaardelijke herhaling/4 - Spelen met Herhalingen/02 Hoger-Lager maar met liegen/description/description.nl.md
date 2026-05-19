## Opgave

Neem het vorige programma maar laat de computer af en toe **liegen**! Zorg ervoor dat er telkens 25% kans is dat de computer je de foute richting op stuurt indien je het getal niet geraden hebt. Met andere woorden dat de computer 'hoger' zegt, terwijl het 'lager' zou moeten zijn. Of omgekeerd.

Om die 25% te programmeren maak je gebruik van onderstaand lijntje code:

```python
if random.randint(1, 4) == 1:
    <leugens>
else:
    <waarheid>
```

Zo kiest de computer een willekeurig getal van 1 tot en met 4 en enkel als die waarde 1 is worden de liegende acties uitgevoerd. Dit komt neer op een kans van 1 op 4 of 25%.

Probeer het zelf uit. Slaag je er zelf nog in om het getal te vinden en de liegende computer te ontmaskeren?