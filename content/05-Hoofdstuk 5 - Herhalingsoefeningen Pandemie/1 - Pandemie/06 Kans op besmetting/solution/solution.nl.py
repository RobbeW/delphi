import math

contacten = int(input("Aantal contacten? "))
kans = int(input("Besmettingskans? "))

besmet = math.floor(contacten * kans / 100)
niet_besmet = contacten - besmet

if kans <= 0 or contacten <= 0:
    minimum_contacten = 0
else:
    minimum_contacten = math.ceil(100 / kans)

print("Verwacht besmet:", besmet)
print("Verwacht niet besmet:", niet_besmet)
print("Minstens 1 verwacht vanaf:", minimum_contacten, "contacten")
