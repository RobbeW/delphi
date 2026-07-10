import math

bericht = input("Bericht? ")
gelovers = int(input("Aantal gelovers? "))

alarmtekens = 0
totaal_gecorrigeerd = 0

for teken in bericht:
    if teken == "!":
        alarmtekens += 1

antwoord = input("Factcheckpercentage of stop? ")
while antwoord != "stop":
    factcheck = int(antwoord)
    gecorrigeerd = math.floor(gelovers * factcheck / 100)
    gelovers -= gecorrigeerd
    totaal_gecorrigeerd += gecorrigeerd
    antwoord = input("Factcheckpercentage of stop? ")

print("Alarmtekens:", alarmtekens)
print("Gecorrigeerd:", totaal_gecorrigeerd)
print("Blijft geloven:", gelovers)
