import math

besmettingen = int(input("Startaantal besmettingen? "))
factor = float(input("Groeifactor? "))
weken = int(input("Aantal weken? "))

start_besmettingen = besmettingen

for week in range(1, weken + 1):
    besmettingen = math.floor(start_besmettingen * (factor ** week))
    print("Week", str(week) + ":", besmettingen, "besmettingen")
