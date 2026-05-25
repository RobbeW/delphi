import math

vatbaar = int(input())
besmet = int(input())
resistent = int(input())
besmettingskracht = int(input())
herstelpercentage = float(input())
max_rondes = int(input())

ronde = 0
while ronde < max_rondes and besmet > 0:
    ronde += 1
    nieuwe_besmettingen = min(vatbaar, besmet * besmettingskracht)
    hersteld = math.floor(besmet * herstelpercentage / 100)
    vatbaar -= nieuwe_besmettingen
    besmet = besmet + nieuwe_besmettingen - hersteld
    resistent += hersteld
    print("Ronde " + str(ronde) + ": vatbaar=" + str(vatbaar) + ", besmet=" + str(besmet) + ", resistent=" + str(resistent))
