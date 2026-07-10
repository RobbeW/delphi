aantal_contacten = int(input("Aantal contacten? "))
risicocontacten = 0

for contact in range(aantal_contacten):
    minuten = int(input("Aantal minuten contact? "))
    beschermd = input("Beschermd? ")
    is_beschermd = beschermd == "ja"
    if minuten >= 15 and not is_beschermd:
        risicocontacten += 1

print("Risicocontacten:", risicocontacten)
