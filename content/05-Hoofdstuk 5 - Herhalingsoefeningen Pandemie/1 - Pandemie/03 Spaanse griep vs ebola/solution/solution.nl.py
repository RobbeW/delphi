import math

spaanse_besmettingen = int(input("Besmettingen Spaanse griep? "))
spaanse_sterfte = float(input("Sterftepercentage Spaanse griep? "))
ebola_besmettingen = int(input("Besmettingen ebola? "))
ebola_sterfte = float(input("Sterftepercentage ebola? "))

spaanse_doden = math.floor(spaanse_besmettingen * spaanse_sterfte / 100)
ebola_doden = math.floor(ebola_besmettingen * ebola_sterfte / 100)

print("Spaanse griep:", spaanse_doden, "verwachte overlijdens")
print("Ebola:", ebola_doden, "verwachte overlijdens")

if spaanse_doden > ebola_doden:
    print("Grootste dodentol: Spaanse griep.")
elif ebola_doden > spaanse_doden:
    print("Grootste dodentol: Ebola.")
else:
    print("Beide ziektes hebben dezelfde verwachte dodentol.")
