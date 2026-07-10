aantal_personen = int(input("Aantal personen? "))
totaal_a = 0
totaal_b = 0

for persoon in range(aantal_personen):
    contacten_a = int(input("Contacten netwerk A? "))
    contacten_b = int(input("Contacten netwerk B? "))
    totaal_a += contacten_a
    totaal_b += contacten_b

print("Netwerk A:", totaal_a, "contacten")
print("Netwerk B:", totaal_b, "contacten")

if totaal_a > totaal_b:
    print("Netwerk A heeft meer contacten.")
elif totaal_b > totaal_a:
    print("Netwerk B heeft meer contacten.")
else:
    print("Beide netwerken hebben evenveel contacten.")
