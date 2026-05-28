import math

vatbaar = int(input("Aantal vatbare personen? "))
besmet = int(input("Aantal besmette personen? "))
resistent = int(input("Aantal resistente personen? "))
besmettingskracht = int(input("Besmettingskracht? "))
herstelpercentage = float(input("Herstelpercentage? "))
max_rondes = int(input("Aantal rondes? "))

ronde = 0
while ronde < max_rondes and besmet > 0:
    ronde += 1
    nieuwe_besmettingen = min(vatbaar, besmet * besmettingskracht)
    hersteld = math.floor(besmet * herstelpercentage / 100)
    vatbaar -= nieuwe_besmettingen
    besmet = besmet + nieuwe_besmettingen - hersteld
    resistent += hersteld
    print("Ronde " + str(ronde) + ": vatbaar=" + str(vatbaar) + ", besmet=" + str(besmet) + ", resistent=" + str(resistent))
