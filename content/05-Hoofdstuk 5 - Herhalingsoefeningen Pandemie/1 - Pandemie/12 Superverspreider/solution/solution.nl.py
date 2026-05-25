import random

personen = int(input())
gewone_besmettingen = int(input())
superverspreiders = 0
totaal = 0

for persoon in range(personen):
    worp = random.randint(1, 10)
    if worp >= 9:
        superverspreiders += 1
        totaal += 25
    else:
        totaal += gewone_besmettingen

print("Superverspreiders:", superverspreiders)
print("Nieuwe besmettingen:", totaal)
