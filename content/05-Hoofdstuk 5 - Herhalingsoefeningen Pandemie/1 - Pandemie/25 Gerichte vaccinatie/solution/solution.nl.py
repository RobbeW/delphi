aantal_personen = int(input("Aantal personen? "))
te_vaccineren = 0
beschermde_contacten = 0

for persoon in range(aantal_personen):
    contacten = int(input("Aantal contacten? "))
    if contacten >= 10:
        te_vaccineren += 1
        beschermde_contacten += contacten

print("Te vaccineren personen:", te_vaccineren)
print("Beschermde contacten:", beschermde_contacten)
