import math

dagen = int(input("Aantal dagen? "))

totaal_vermeden = 0
totaal_met_maskers = 0

for dag in range(dagen):
    verwacht = int(input("Verwachte besmettingen zonder maskers? "))
    effect = int(input("Beschermingspercentage? "))

    vermeden = math.floor(verwacht * effect / 100)
    met_maskers = verwacht - vermeden

    totaal_vermeden += vermeden
    totaal_met_maskers += met_maskers

print("Totaal vermeden besmettingen:", totaal_vermeden)
print("Totaal met mondmaskers:", totaal_met_maskers)
