import math

r0 = float(input())
besmettingen = int(input())
populatie = int(input())

cyclus = 0

if besmettingen >= populatie:
    print("De volledige populatie is al besmet.")
else:
    while besmettingen < populatie:
        nieuwe_besmettingen = math.floor(besmettingen * r0)

        if nieuwe_besmettingen == 0:
            print("De epidemie dooft uit na", cyclus, "cycli met", besmettingen, "besmettingen.")
            break

        if besmettingen + nieuwe_besmettingen > populatie:
            nieuwe_besmettingen = populatie - besmettingen

        besmettingen += nieuwe_besmettingen
        cyclus += 1
        print("Na", cyclus, "cycli zijn er", besmettingen, "besmettingen.")
