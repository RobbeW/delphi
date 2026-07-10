clusters = int(input("Aantal clusters? "))
totaal = 0

for cluster in range(1, clusters + 1):
    besmet = int(input("Aantal besmette personen? "))
    nieuwe_besmettingen = besmet * 2
    totaal += nieuwe_besmettingen
    print("Cluster", str(cluster) + ":", nieuwe_besmettingen, "nieuwe besmettingen")

print("Totaal:", totaal, "nieuwe besmettingen")
