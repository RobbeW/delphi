import math

populatie = int(input())
per_week = int(input())
doelpercentage = float(input())

doel = math.ceil(populatie * doelpercentage / 100)
gevaccineerd = 0
week = 0

while gevaccineerd < doel and gevaccineerd < populatie:
    week += 1
    gevaccineerd += per_week
    if gevaccineerd > populatie:
        gevaccineerd = populatie
    print("Week", str(week) + ":", gevaccineerd, "mensen gevaccineerd")

print("Nog vatbaar:", populatie - gevaccineerd)
