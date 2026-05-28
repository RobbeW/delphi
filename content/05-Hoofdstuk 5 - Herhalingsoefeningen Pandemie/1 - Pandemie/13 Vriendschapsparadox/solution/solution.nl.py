aantal_personen = int(input("Aantal personen? "))
vriendenlijst = []
totaal = 0
maximum = -1
populairste = 0

for persoon in range(1, aantal_personen + 1):
    vrienden = int(input("Aantal vrienden? "))
    vriendenlijst.append(vrienden)
    totaal += vrienden
    if vrienden > maximum:
        maximum = vrienden
        populairste = persoon

gemiddelde = round(totaal / aantal_personen, 2)
onder_gemiddelde = 0
for vrienden in vriendenlijst:
    if vrienden < gemiddelde:
        onder_gemiddelde += 1

print("Gemiddeld aantal vrienden:", gemiddelde)
print("Populairste persoon:", populairste, "met", maximum, "vrienden.")
print("Aantal personen onder het gemiddelde:", onder_gemiddelde)
