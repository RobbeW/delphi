import random

contacten = int(input("Aantal contacten? "))
kans = int(input("Besmettingskans? "))
besmet = 0

for contact in range(contacten):
    worp = random.randint(1, 100)
    if worp <= kans:
        besmet += 1

print("Besmet:", besmet)
print("Niet besmet:", contacten - besmet)
