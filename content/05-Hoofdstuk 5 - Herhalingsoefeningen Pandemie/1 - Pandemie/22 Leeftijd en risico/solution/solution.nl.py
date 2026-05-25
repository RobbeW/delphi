aantal_personen = int(input())
hoog_risico = 0

for persoon in range(1, aantal_personen + 1):
    leeftijd = int(input())
    gevaccineerd = input() == "ja"
    chronisch = input() == "ja"

    score = 0
    if leeftijd >= 65:
        score += 2
    elif leeftijd >= 45:
        score += 1
    if not gevaccineerd:
        score += 1
    if chronisch:
        score += 2

    if score >= 4:
        risico = "hoog"
        hoog_risico += 1
    elif score >= 2:
        risico = "matig"
    else:
        risico = "laag"

    print("Persoon " + str(persoon) + ": score " + str(score) + ", risico " + risico)

print("Aantal hoog risico:", hoog_risico)
