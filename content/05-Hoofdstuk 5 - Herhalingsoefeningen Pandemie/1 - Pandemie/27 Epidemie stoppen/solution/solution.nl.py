r0 = float(input("R0? "))
populatie = int(input("Populatie? "))
prikken_per_ronde = int(input("Vaccinaties per ronde? "))

gevaccineerd = 0
rondes = 0
r = round(r0, 2)

print("Start: 0 gevaccineerd, R =", r)

while r >= 1 and gevaccineerd < populatie:
    rondes += 1
    gevaccineerd += prikken_per_ronde
    if gevaccineerd > populatie:
        gevaccineerd = populatie

    r = r0 * (1 - gevaccineerd / populatie)
    r = round(r, 2)
    print("Ronde " + str(rondes) + ": " + str(gevaccineerd) + " gevaccineerd, R = " + str(r))

print("De epidemie stopt na", rondes, "vaccinatierondes.")
