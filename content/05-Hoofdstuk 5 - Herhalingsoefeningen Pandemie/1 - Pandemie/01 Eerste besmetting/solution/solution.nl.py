aantal_wijken = int(input())
totaal = 0
maximum = -1
zwaarste_wijk = 0

for wijk in range(1, aantal_wijken + 1):
    besmettingen = int(input())
    totaal += besmettingen
    if besmettingen > maximum:
        maximum = besmettingen
        zwaarste_wijk = wijk

print("Totaal besmet:", totaal)
print("Zwaarst getroffen wijk:", zwaarste_wijk, "met", maximum, "besmettingen.")

if totaal >= 100 or maximum >= 50:
    print("Status: opschalen.")
else:
    print("Status: opvolgen.")
