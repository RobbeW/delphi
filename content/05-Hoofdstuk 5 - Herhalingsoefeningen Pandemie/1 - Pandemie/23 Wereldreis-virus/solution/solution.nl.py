steden = int(input("Aantal steden? "))
reizigers = int(input("Besmette reizigers in eerste stad? "))
lokale_besmettingen = int(input("Lokale besmettingen per stad? "))

for stad in range(1, steden + 1):
    reizigers += lokale_besmettingen
    print("Stad " + str(stad) + ": " + str(reizigers) + " besmettingen")
