import math

huidig = int(input())
factor = float(input())
dagen = int(input())
limiet = int(input())

totaal = huidig
dag = 0

while dag < dagen and totaal < limiet and huidig > 0:
    dag += 1
    huidig = math.floor(huidig * factor)
    if totaal + huidig > limiet:
        huidig = limiet - totaal
    totaal += huidig
    print("Dag " + str(dag) + ": " + str(huidig) + " nieuwe deelnemers, " + str(totaal) + " totaal")

if totaal >= limiet:
    print("De challenge gaat viraal na dag " + str(dag) + ".")
else:
    print("Na", dag, "dagen zijn er", totaal, "deelnemers bereikt.")
