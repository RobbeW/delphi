naam = input()
totaal = 0
risicocontacten = 0
langste_naam = ""
langste_minuten = -1

while naam != "stop":
    minuten = int(input())
    totaal += 1
    if minuten >= 15:
        risicocontacten += 1
    if minuten > langste_minuten:
        langste_minuten = minuten
        langste_naam = naam
    naam = input()

print("Er zijn", totaal, "contacten genoteerd.")
print("Risicocontacten:", risicocontacten)
if totaal == 0:
    print("Geen risicocontact gevonden.")
else:
    print("Langste contact:", langste_naam, "(" + str(langste_minuten) + " minuten)")
