deelnemers = int(input("Startaantal deelnemers? "))
factor = int(input("Verspreidingsfactor? "))
dagen = int(input("Aantal dagen? "))

for dag in range(1, dagen + 1):
    deelnemers *= factor
    print("Dag " + str(dag) + ": " + str(deelnemers) + " deelnemers")
