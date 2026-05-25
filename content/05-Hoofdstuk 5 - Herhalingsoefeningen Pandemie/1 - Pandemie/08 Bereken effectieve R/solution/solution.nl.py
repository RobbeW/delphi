import math

r0 = float(input())
vaccinatie = float(input())
maskers = float(input())
besmettingen = int(input())
max_cycli = int(input())

effectieve_r = r0 * (1 - vaccinatie / 100) * (1 - maskers / 100)
effectieve_r = round(effectieve_r, 2)

print("Effectieve R:", effectieve_r)

if effectieve_r > 1:
    print("De epidemie groeit.")
elif effectieve_r < 1:
    print("De epidemie krimpt.")
else:
    print("De epidemie blijft stabiel.")

cyclus = 0
while cyclus < max_cycli and besmettingen > 0:
    cyclus += 1
    nieuwe_besmettingen = math.floor(besmettingen * effectieve_r)
    print("Cyclus", str(cyclus) + ":", nieuwe_besmettingen, "nieuwe besmettingen")
    besmettingen = nieuwe_besmettingen
