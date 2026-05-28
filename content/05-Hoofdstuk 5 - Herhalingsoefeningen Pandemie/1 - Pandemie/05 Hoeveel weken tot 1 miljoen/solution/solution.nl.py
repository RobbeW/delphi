import math

besmettingen = int(input("Startaantal besmettingen? "))
factor = float(input("Groeifactor? "))
grens = int(input("Grens? "))

weken = 0

while besmettingen < grens:
    volgende = math.floor(besmettingen * factor)
    if volgende <= besmettingen:
        print("De grens wordt niet bereikt. Na", weken, "weken zijn er", besmettingen, "besmettingen.")
        break
    besmettingen = volgende
    weken += 1
else:
    print("Na", weken, "weken zijn er", besmettingen, "besmettingen.")
