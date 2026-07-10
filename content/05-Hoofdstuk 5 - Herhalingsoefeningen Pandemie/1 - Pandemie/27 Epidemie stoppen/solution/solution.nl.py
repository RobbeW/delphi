r0 = float(input("R0? "))
aantal_scenarios = int(input("Aantal scenario's? "))

stopt = 0

for scenario in range(aantal_scenarios):
    vaccinatie = float(input("Vaccinatiepercentage? "))
    effectieve_r = r0 * (1 - vaccinatie / 100)
    effectieve_r = round(effectieve_r, 2)

    if effectieve_r < 1:
        stopt += 1

print("Scenario's waarin de epidemie stopt:", stopt)
