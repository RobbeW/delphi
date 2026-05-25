clusters = int(input())
totaal = 0

for cluster in range(1, clusters + 1):
    grootte = int(input())
    besmet = int(input())
    vatbaar = grootte - besmet
    nieuwe_besmettingen = min(vatbaar, besmet * 2)
    totaal += nieuwe_besmettingen
    print("Cluster", str(cluster) + ":", nieuwe_besmettingen, "nieuwe besmettingen")

print("Totaal:", totaal, "nieuwe besmettingen")
