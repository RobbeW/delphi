clusters = int(input("Aantal clusters? "))
totaal = 0

for cluster in range(1, clusters + 1):
    grootte = int(input("Grootte van cluster? "))
    besmet = int(input("Aantal besmette leerlingen in cluster? "))
    vatbaar = grootte - besmet
    nieuwe_besmettingen = min(vatbaar, besmet * 2)
    totaal += nieuwe_besmettingen
    print("Cluster", str(cluster) + ":", nieuwe_besmettingen, "nieuwe besmettingen")

print("Totaal:", totaal, "nieuwe besmettingen")
