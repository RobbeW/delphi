r0 = float(input("Startwaarde R0? "))
mutaties = int(input("Aantal mutaties? "))

nieuwe_r0 = r0

for mutatie in range(mutaties):
    verandering = float(input("Verandering? "))
    nieuwe_r0 = round(nieuwe_r0 + verandering, 2)

print("Nieuwe R0:", nieuwe_r0)
if nieuwe_r0 > r0:
    print("De variant wordt sterker.")
elif nieuwe_r0 < r0:
    print("De variant wordt zwakker.")
else:
    print("De variant blijft stabiel.")
