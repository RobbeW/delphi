import math

steden = int(input())
reizigers = int(input())
r0 = float(input())
reispercentage = float(input())

for stad in range(1, steden + 1):
    lokale_besmettingen = math.floor(reizigers * r0)
    totaal_stad = reizigers + lokale_besmettingen
    print("Stad " + str(stad) + ": " + str(lokale_besmettingen) + " lokale besmettingen, " + str(totaal_stad) + " totaal")

    if stad < steden:
        reizigers = math.floor(totaal_stad * reispercentage / 100)
        if reizigers < 1 and totaal_stad > 0:
            reizigers = 1
        print("Naar stad", stad + 1, "reizen", reizigers, "besmette personen.")
