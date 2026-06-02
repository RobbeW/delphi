r0 = float(input("R0? "))
vaccinatie = float(input("Vaccinatiepercentage? "))

effectieve_r = r0 * (1 - vaccinatie / 100)
effectieve_r = round(effectieve_r, 2)

print("Effectieve R:", effectieve_r)

if effectieve_r > 1:
    print("De epidemie groeit.")
elif effectieve_r < 1:
    print("De epidemie krimpt.")
else:
    print("De epidemie blijft stabiel.")
