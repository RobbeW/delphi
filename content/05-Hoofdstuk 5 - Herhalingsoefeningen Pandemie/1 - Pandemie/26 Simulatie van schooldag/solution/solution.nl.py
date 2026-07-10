leerlingen = int(input("Klasgrootte? "))
besmet = int(input("Startbesmettingen? "))
lessen = int(input("Aantal lessen? "))

if besmet > leerlingen:
    besmet = leerlingen

for les in range(lessen):
    vatbaar = leerlingen - besmet
    nieuwe_besmettingen = min(vatbaar, besmet)
    besmet += nieuwe_besmettingen

print("Na", lessen, "lessen zijn er", besmet, "besmettingen.")
