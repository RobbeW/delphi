import math

capaciteit = int(input("Capaciteit? "))
bezet = int(input("Bezette bedden? "))
opnames = int(input("Nieuwe opnames? "))
oppervlakte = float(input("Oppervlakte triagezone? "))

bezet += opnames
straal = round(math.sqrt(oppervlakte / math.pi), 2)

print("Bezette bedden:", bezet)
print("Straal triagezone:", straal)
if bezet > capaciteit:
    print("Code rood.")
else:
    print("Genoeg capaciteit.")
