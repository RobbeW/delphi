aantal_groepen = int(input("Aantal groepen? "))
dosissen_per_persoon = int(input("Dosissen per persoon? "))
voorraad = int(input("Voorraad? "))

nodig = 0

for groep in range(aantal_groepen):
    personen = int(input("Aantal personen? "))
    nodig += personen * dosissen_per_persoon

print("Nodige dosissen:", nodig)
if voorraad >= nodig:
    print("Er zijn genoeg dosissen.")
else:
    print("Tekort:", nodig - voorraad)
