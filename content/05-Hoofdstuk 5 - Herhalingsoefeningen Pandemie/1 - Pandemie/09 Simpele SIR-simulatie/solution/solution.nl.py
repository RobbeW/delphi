vatbaar = int(input("Aantal vatbare personen? "))
besmet = int(input("Aantal besmette personen? "))
resistent = int(input("Aantal resistente personen? "))
rondes = int(input("Aantal rondes? "))

for ronde in range(rondes):
    nieuwe_besmettingen = int(input("Nieuwe besmettingen? "))
    genezen = int(input("Genezen personen? "))

    vatbaar -= nieuwe_besmettingen
    besmet = besmet + nieuwe_besmettingen - genezen
    resistent += genezen

print("Na", rondes, "rondes: vatbaar=" + str(vatbaar) + ", besmet=" + str(besmet) + ", resistent=" + str(resistent))
