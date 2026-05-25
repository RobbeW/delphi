aantal_personen = int(input())
vaccins = int(input())
contacten = []

for persoon in range(aantal_personen):
    contacten.append(int(input()))

beschermde_contacten = 0
gezet = 0

while vaccins > 0:
    maximum = -1
    index = -1
    for i in range(len(contacten)):
        if contacten[i] > maximum:
            maximum = contacten[i]
            index = i
    if maximum <= 0:
        break
    gezet += 1
    beschermde_contacten += maximum
    print("Vaccin " + str(gezet) + ": persoon " + str(index + 1) + " met " + str(maximum) + " contacten")
    contacten[index] = -1
    vaccins -= 1

print("Beschermde contacten:", beschermde_contacten)
