import random

resistent = int(input())
rondes = int(input())
kans = int(input())
totaal = 0
ronde = 0

while ronde < rondes and resistent > 0:
    ronde += 1
    herinfecties = 0
    for persoon in range(resistent):
        if random.randint(1, 100) <= kans:
            herinfecties += 1
    resistent -= herinfecties
    totaal += herinfecties
    print("Ronde " + str(ronde) + ": " + str(herinfecties) + " herinfecties, " + str(resistent) + " resistent")

print("Totaal herinfecties:", totaal)
