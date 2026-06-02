import math

besmettingen = int(input("Startaantal besmettingen? "))
factor = float(input("Groeifactor? "))

grens = 1000000
weken = 0

while besmettingen < grens:
    besmettingen = math.floor(besmettingen * factor)
    weken += 1

print("Na", weken, "weken zijn er", besmettingen, "besmettingen.")
