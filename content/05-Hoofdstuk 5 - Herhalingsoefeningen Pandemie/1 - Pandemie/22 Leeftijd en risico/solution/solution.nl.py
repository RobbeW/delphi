aantal_personen = int(input("Aantal personen? "))

laag = 0
matig = 0
hoog = 0

for persoon in range(aantal_personen):
    leeftijd = int(input("Leeftijd? "))

    if leeftijd >= 65:
        hoog += 1
    elif leeftijd >= 45:
        matig += 1
    else:
        laag += 1

print("Laag risico:", laag)
print("Matig risico:", matig)
print("Hoog risico:", hoog)
