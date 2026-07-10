# Invoer

lengte = float(input("Voer de lengte in: "))
breedte = float(input("Voer de breedte in: "))


# Verwerking

omtrek = round(2 * (lengte + breedte), 2)
oppervlakte = round(lengte * breedte, 2)


# Uitvoer

print("De omtrek bedraagt:", omtrek, "cm.")
print("De oppervlakte bedraagt:", oppervlakte, "cm².")
