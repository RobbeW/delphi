populatie = int(input("Populatie? "))
per_week = int(input("Vaccinaties per week? "))
weken = int(input("Aantal weken? "))

gevaccineerd = 0

for week in range(weken):
    gevaccineerd += per_week
    if gevaccineerd > populatie:
        gevaccineerd = populatie

controles = 0
for week in range(2, weken + 1, 2):
    controles += 1

print("Gevaccineerd:", gevaccineerd)
print("Nog vatbaar:", populatie - gevaccineerd)
print("Controles:", controles)
