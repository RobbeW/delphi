aantal_wijken = int(input("Hoeveel wijken? "))
totaal = 0
max_besmettingen = -1
max_wijk = 0

for wijk in range(1, aantal_wijken + 1):
    besmettingen = int(input("Aantal besmettingen in deze wijk? "))
    totaal += besmettingen
    if besmettingen > max_besmettingen:
        max_besmettingen = besmettingen
        max_wijk = wijk

print("Totaal besmet:", totaal)
print("Zwaarst getroffen wijk:", max_wijk, "met", max_besmettingen, "besmettingen.")

if totaal >= 20:
    print("Status: opvolgen.")
else:
    print("Status: rustig.")
