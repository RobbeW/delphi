import math

bevolking = int(input("Aantal personen? "))
dosissen_per_persoon = int(input("Dosissen per persoon? "))
dosissen_per_flacon = int(input("Dosissen per flacon? "))
flacons_per_doos = int(input("Flacons per doos? "))

nodige_dosissen = bevolking * dosissen_per_persoon
nodige_flacons = math.ceil(nodige_dosissen / dosissen_per_flacon)
volle_dozen = nodige_flacons // flacons_per_doos
losse_flacons = nodige_flacons % flacons_per_doos

if losse_flacons == 0:
    te_bestellen_dozen = volle_dozen
else:
    te_bestellen_dozen = volle_dozen + 1

print("Nodige dosissen:", nodige_dosissen)
print("Nodige flacons:", nodige_flacons)
print("Volle dozen:", volle_dozen)
print("Losse flacons:", losse_flacons)
print("Te bestellen dozen:", te_bestellen_dozen)
