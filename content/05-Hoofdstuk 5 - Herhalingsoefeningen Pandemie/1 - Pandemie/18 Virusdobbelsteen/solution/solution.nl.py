import random

beurten = int(input("Aantal beurten? "))

totaal = 0

for beurt in range(beurten):
    worp = random.randint(1, 6)
    totaal += worp

print("Na", beurten, "beurten zijn er", totaal, "besmettingen.")
