resistent = int(input("Aantal resistente personen? "))
per_ronde = int(input("Herinfecties per ronde? "))
rondes = int(input("Aantal rondes? "))

totaal = 0

for ronde in range(rondes):
    if resistent > 0:
        herinfecties = per_ronde
        if herinfecties > resistent:
            herinfecties = resistent
        resistent -= herinfecties
        totaal += herinfecties

print("Totaal herinfecties:", totaal)
print("Nog resistent:", resistent)
