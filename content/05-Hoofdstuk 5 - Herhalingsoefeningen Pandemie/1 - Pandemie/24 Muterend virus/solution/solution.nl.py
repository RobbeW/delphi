import math
import random

r0 = float(input())
besmettingen = int(input())
cycli = int(input())

totaal = besmettingen

for cyclus in range(1, cycli + 1):
    mutatie = random.randint(1, 3)
    variant = "stabiel"

    if mutatie == 1:
        r0 = max(0.0, r0 - 0.25)
        variant = "zwakker"
    elif mutatie == 3:
        r0 += 0.4
        variant = "besmettelijker"

    r0 = round(r0, 2)
    nieuwe_besmettingen = math.floor(besmettingen * r0)
    totaal += nieuwe_besmettingen
    besmettingen = nieuwe_besmettingen

    print("Cyclus " + str(cyclus) + ": variant " + variant + ", R0 = " + str(r0) + ", nieuwe besmettingen = " + str(nieuwe_besmettingen) + ", totaal = " + str(totaal))

if besmettingen == 0:
    print("De uitbraak dooft uit.")
elif r0 > 1:
    print("De variant blijft groeien.")
else:
    print("De variant verzwakt.")
