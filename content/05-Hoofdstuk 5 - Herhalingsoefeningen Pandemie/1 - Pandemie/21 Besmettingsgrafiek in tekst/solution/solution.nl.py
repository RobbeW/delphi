import math

weken = int(input("Aantal weken? "))
besmettingen = int(input("Startaantal besmettingen? "))
factor = float(input("Groeifactor? "))
schaal = int(input("Schaal per ster? "))

for week in range(1, weken + 1):
    aantal_sterren = besmettingen // schaal
    if aantal_sterren == 0 and besmettingen > 0:
        aantal_sterren = 1
    grafiek = ""
    for ster in range(aantal_sterren):
        grafiek += "*"
    print("Week " + str(week) + " (" + str(besmettingen) + "): " + grafiek)
    besmettingen = math.floor(besmettingen * factor)
