klassen = int(input())
lessen = int(input())
leerlingen = int(input())
start_besmet = int(input())

totaal = 0
for klas in range(1, klassen + 1):
    besmet = start_besmet
    if besmet > leerlingen:
        besmet = leerlingen
    vatbaar = leerlingen - besmet
    for les in range(1, lessen + 1):
        nieuwe_besmettingen = min(vatbaar, besmet)
        besmet += nieuwe_besmettingen
        vatbaar -= nieuwe_besmettingen
    totaal += besmet
    print("Klas " + str(klas) + ": " + str(besmet) + " besmet na " + str(lessen) + " lessen")

print("Totaal op school:", totaal, "besmettingen")
