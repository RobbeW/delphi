import math

besmettingen = int(input("Startaantal besmettingen? "))
factor = float(input("Groeifactor? "))
weken = int(input("Aantal weken? "))
grens = int(input("Alarmgrens? "))

if besmettingen >= grens:
    print("De grens is al bereikt.")
else:
    for week in range(1, weken + 1):
        besmettingen = math.floor(besmettingen * factor)
        if besmettingen > grens:
            besmettingen = grens
        print("Week", str(week) + ":", besmettingen, "besmettingen")
        if besmettingen >= grens:
            print("De grens wordt bereikt na week", str(week) + ".")
            break
