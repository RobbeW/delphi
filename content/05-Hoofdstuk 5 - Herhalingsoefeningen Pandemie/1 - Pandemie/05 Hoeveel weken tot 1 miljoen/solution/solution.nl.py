import math

besmettingen = int(input())
factor = float(input())
grens = int(input())

weken = 0

while besmettingen <= grens:
    volgende = math.floor(besmettingen * factor)
    if volgende <= besmettingen:
        print("De grens wordt niet bereikt. Na", weken, "weken zijn er", besmettingen, "besmettingen.")
        break
    besmettingen = volgende
    weken += 1
else:
    print("Na", weken, "weken zijn er", besmettingen, "besmettingen.")
