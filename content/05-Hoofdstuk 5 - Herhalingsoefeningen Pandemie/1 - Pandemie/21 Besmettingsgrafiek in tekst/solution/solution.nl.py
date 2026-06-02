weken = int(input("Aantal weken? "))
schaal = int(input("Schaal per ster? "))

for week in range(1, weken + 1):
    besmettingen = int(input("Aantal besmettingen? "))
    aantal_sterren = besmettingen // schaal
    rest = besmettingen % schaal
    if aantal_sterren == 0 and besmettingen > 0:
        aantal_sterren = 1
    grafiek = "*" * aantal_sterren
    if rest > 0 and besmettingen >= schaal:
        grafiek += "+"
    print("Week " + str(week) + ": " + grafiek)
