import random

grens = int(input())
max_beurten = int(input())
totaal = 0
beurt = 0

while beurt < max_beurten and totaal < grens:
    worp = random.randint(1, 6)
    beurt += 1
    totaal += worp
    print("Beurt " + str(beurt) + ": +" + str(worp) + " besmettingen, totaal " + str(totaal))

if totaal >= grens:
    print("De uitbraak bereikt de grens na", beurt, "beurten.")
else:
    print("Na", beurt, "beurten zijn er", totaal, "besmettingen.")
