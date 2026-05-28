import math

gelovers = int(input("Startaantal gelovers? "))
factor = float(input("Verspreidingsfactor? "))
factcheck = float(input("Factcheckpercentage? "))
max_rondes = int(input("Aantal rondes? "))
grens = int(input("Virale grens? "))

ronde = 0

while ronde < max_rondes and gelovers > 0 and gelovers < grens:
    ronde += 1
    gedeeld = math.floor(gelovers * factor)
    gecorrigeerd = math.floor(gedeeld * factcheck / 100)
    gelovers = gedeeld - gecorrigeerd
    print("Ronde " + str(ronde) + ": " + str(gelovers) + " mensen geloven het gerucht.")

if gelovers >= grens:
    print("Het gerucht gaat viraal na", ronde, "rondes.")
elif gelovers == 0:
    print("Het gerucht dooft uit na", ronde, "rondes.")
else:
    print("Na", ronde, "rondes is het gerucht nog niet viraal.")
