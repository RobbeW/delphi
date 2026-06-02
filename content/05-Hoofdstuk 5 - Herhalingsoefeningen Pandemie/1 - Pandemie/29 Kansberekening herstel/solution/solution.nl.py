import math

aantal_groepen = int(input("Aantal groepen? "))

totaal_genezen = 0
totaal_nog_ziek = 0

for groep in range(aantal_groepen):
    ziek = int(input("Aantal zieken? "))
    kans = int(input("Herstelkans? "))

    genezen = math.floor(ziek * kans / 100)
    nog_ziek = ziek - genezen

    totaal_genezen += genezen
    totaal_nog_ziek += nog_ziek

print("Genezen:", totaal_genezen)
print("Nog ziek:", totaal_nog_ziek)
