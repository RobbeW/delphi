personen = int(input("Aantal personen? "))
rondes = int(input("Aantal rondes? "))
gelijke_contacten = int(input("Contacten gelijk netwerk? "))
hub_contacten = int(input("Contacten hub? "))
kleine_contacten = int(input("Contacten gewone personen? "))

gelijk_besmet = 1
ongelijk_besmet = 1

for ronde in range(1, rondes + 1):
    nieuw_gelijk = min(personen - gelijk_besmet, gelijk_besmet * gelijke_contacten // 10)
    nieuw_ongelijk = min(personen - ongelijk_besmet, (hub_contacten + (ongelijk_besmet - 1) * kleine_contacten) // 10)
    gelijk_besmet += nieuw_gelijk
    ongelijk_besmet += nieuw_ongelijk
    print("Ronde " + str(ronde) + ": gelijk=" + str(gelijk_besmet) + ", ongelijk=" + str(ongelijk_besmet))

if gelijk_besmet > ongelijk_besmet:
    print("Het gelijke netwerk verspreidt sneller.")
elif ongelijk_besmet > gelijk_besmet:
    print("Het ongelijke netwerk verspreidt sneller.")
else:
    print("Beide netwerken verspreiden even snel.")
