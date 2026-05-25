dagen = int(input("Aantal dagen? "))
effect = float(input("Beschermingspercentage? "))
totaal = 0

for dag in range(1, dagen + 1):
    verwacht = int(input("Verwachte besmettingen zonder maskers? "))
    vermeden = round(verwacht * effect / 100, 2)
    totaal += vermeden
    print("Dag " + str(dag) + ": " + str(vermeden) + " besmettingen vermeden")

totaal = round(totaal, 2)
print("Totaal vermeden:", totaal)
