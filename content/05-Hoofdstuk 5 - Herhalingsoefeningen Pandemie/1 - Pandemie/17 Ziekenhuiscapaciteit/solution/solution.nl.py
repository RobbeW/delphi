capaciteit = int(input())
bezet = int(input())
dagen = int(input())
eerste_rood = 0

for dag in range(1, dagen + 1):
    opnames = int(input())
    ontslagen = int(input())
    bezet += opnames - ontslagen
    if bezet < 0:
        bezet = 0
    print("Dag " + str(dag) + ": " + str(bezet) + " bedden bezet")
    if bezet > capaciteit and eerste_rood == 0:
        eerste_rood = dag

if eerste_rood > 0:
    print("Code rood op dag " + str(eerste_rood) + ".")
else:
    print("Geen overbelasting.")
