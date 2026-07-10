aantal_personen = int(input("Aantal personen? "))
totaal = 0

for persoon in range(1, aantal_personen + 1):
    positieve_test = input("Positieve test? ") == "ja"
    if positieve_test:
        totaal += 1
        print("Persoon " + str(persoon) + ": quarantaine")
    else:
        print("Persoon " + str(persoon) + ": geen quarantaine")

print("Totaal in quarantaine:", totaal)
