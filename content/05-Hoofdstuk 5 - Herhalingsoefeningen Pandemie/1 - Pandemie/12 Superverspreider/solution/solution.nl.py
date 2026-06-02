aantal_groepen = int(input("Aantal groepen? "))

totaal_superverspreiders = 0
totaal = 0

for groep in range(aantal_groepen):
    gewone_personen = int(input("Gewone besmette personen? "))
    superverspreiders = int(input("Aantal superverspreiders? "))

    totaal_superverspreiders += superverspreiders
    totaal += gewone_personen * 2 + superverspreiders * 25

print("Superverspreiders:", totaal_superverspreiders)
print("Nieuwe besmettingen:", totaal)
