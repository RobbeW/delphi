import random

ziek = int(input("Startaantal zieken? "))
kans = int(input("Herstelkans? "))
max_dagen = int(input("Aantal dagen? "))
totaal_genezen = 0
dag = 0

while dag < max_dagen and ziek > 0:
    dag += 1
    genezen = 0
    for patient in range(ziek):
        if random.randint(1, 100) <= kans:
            genezen += 1
    ziek -= genezen
    totaal_genezen += genezen
    print("Dag " + str(dag) + ": " + str(genezen) + " genezen, " + str(ziek) + " ziek")

print("Totaal genezen:", totaal_genezen)
