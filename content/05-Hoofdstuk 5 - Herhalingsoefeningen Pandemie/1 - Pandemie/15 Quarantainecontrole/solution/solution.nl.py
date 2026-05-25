aantal_personen = int(input())
totaal = 0

for persoon in range(1, aantal_personen + 1):
    symptomen = input() == "ja"
    positieve_test = input() == "ja"
    risicocontact = input() == "ja"
    gevaccineerd = input() == "ja"

    quarantaine = positieve_test or (symptomen and risicocontact and not gevaccineerd)
    if quarantaine:
        totaal += 1
        print("Persoon " + str(persoon) + ": quarantaine")
    else:
        print("Persoon " + str(persoon) + ": geen quarantaine")

print("Totaal in quarantaine:", totaal)
