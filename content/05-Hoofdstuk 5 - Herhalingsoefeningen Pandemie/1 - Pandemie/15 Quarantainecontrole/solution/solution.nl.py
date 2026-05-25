aantal_personen = int(input("Aantal personen? "))
totaal = 0

for persoon in range(1, aantal_personen + 1):
    symptomen = input("Symptomen? ") == "ja"
    positieve_test = input("Positieve test? ") == "ja"
    risicocontact = input("Risicocontact? ") == "ja"
    gevaccineerd = input("Gevaccineerd? ") == "ja"

    quarantaine = positieve_test or (symptomen and risicocontact and not gevaccineerd)
    if quarantaine:
        totaal += 1
        print("Persoon " + str(persoon) + ": quarantaine")
    else:
        print("Persoon " + str(persoon) + ": geen quarantaine")

print("Totaal in quarantaine:", totaal)
