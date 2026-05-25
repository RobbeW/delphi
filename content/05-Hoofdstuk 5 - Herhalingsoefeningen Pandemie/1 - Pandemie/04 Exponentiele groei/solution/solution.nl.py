import math

besmettingen = int(input())
factor = float(input())
weken = int(input())
grens = int(input())

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
