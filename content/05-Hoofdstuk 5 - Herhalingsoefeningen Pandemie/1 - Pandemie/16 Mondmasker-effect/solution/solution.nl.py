dagen = int(input())
effect = float(input())
totaal = 0

for dag in range(1, dagen + 1):
    verwacht = int(input())
    vermeden = round(verwacht * effect / 100, 2)
    totaal += vermeden
    print("Dag " + str(dag) + ": " + str(vermeden) + " besmettingen vermeden")

totaal = round(totaal, 2)
print("Totaal vermeden:", totaal)
