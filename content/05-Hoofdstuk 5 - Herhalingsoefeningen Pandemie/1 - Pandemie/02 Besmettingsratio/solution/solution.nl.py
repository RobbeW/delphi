r0 = int(input("R0? "))
besmettingen = int(input("Startaantal besmettingen? "))
cycli = int(input("Aantal cycli? "))

for cyclus in range(1, cycli + 1):
    nieuwe_besmettingen = besmettingen * r0
    besmettingen += nieuwe_besmettingen
    print("Na", cyclus, "cycli zijn er", besmettingen, "besmettingen.")
