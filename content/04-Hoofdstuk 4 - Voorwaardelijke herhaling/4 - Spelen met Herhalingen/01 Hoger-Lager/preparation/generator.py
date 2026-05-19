import os
import subprocess
import importlib
import random
import math
import json

# set fixed seed for generating test cases
random.seed(123456789)

# locate evaldir
evaldir = os.path.join("..", "evaluation")
if not os.path.exists(evaldir):
    os.makedirs(evaldir)

# locate solutiondir
solutiondir = os.path.join("..", "solution")
if not os.path.exists(solutiondir):
    os.makedirs(solutiondir)

def write_json( data:dict ):
    """ A function to write JSON file"""
    with open(os.path.join("..", "evaluation", "tests.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent = 2)

# generate test data
ntests = 20
cases = [ ]

while len( cases ) < ntests:
    seed = random.randint(1,10000)
    cases.append( (seed, ) )
    
# generate unit tests for functions
exportdata = {"tabs": [] }
exportdata["tabs"].append( {"name": "Feedback",
                            "contexts": [] } )

i = -1

for test in cases:
    exportdata["tabs"][0]["contexts"].append({})
    i += 1    
    seed = test[0]
    # generate before expression
    beforecase = {"python": {"data": "import random; random.seed("+str(seed)+")"}}
    exportdata["tabs"][0]["contexts"][i]["before"] = beforecase
     
    exportdata["tabs"][0]["contexts"][i]["testcases"] = []
    
    # generate test expression        
    testcase = {"description": "",
                "input": {},
                "output": {} }
    
    # generate output to output file
    random.seed(seed)
    inputtxt = ""
    outputtxt = ""
    
    gokken = []
    getal = random.randint( 1, 1000 )

    aantal = 0
    if random.randint(0,5) == 0:
        inputtxt += str(getal)+"\n"
        outputtxt += "Je hebt "+ str(getal) +" meteen geraden!\n"
        gokken.append(getal)
    else:
        geraden = False
        a = 1000
        b = 1
        while not geraden:
            gok = (a + b)//2
            inputtxt += str(gok) + "\n"
            gokken.append(gok)
            aantal += 1
            if gok > getal:
                outputtxt += "Het getal is lager dan "+str(gok)+"\n"
                a = gok
            elif gok < getal:
                outputtxt += "Het getal is hoger dan "+str(gok)+"\n"
                b = gok
            else:
                geraden = True
        outputtxt += "Je hebt "+str(getal)+" geraden in " + str(aantal) + " pogingen!\n"
    
    # setup for return expressions
    if len(gokken) != 1:
        gokjes_txt = ', '.join(map(str, gokken)) 
        testcase["description"] = "Uitvoeren met seed "+str(seed)+" en gokken "+ gokjes_txt +" leidt tot:"
    else:
        testcase["description"] = "Uitvoeren met seed "+str(seed)+" en gok "+ str(gokken[0]) +" leidt tot:"
    testcase["input"]["stdin"] = {"type": "text", 
                                  "data": inputtxt }
    testcase["output"]["stdout"] = {"type": "text", 
                                    "data": outputtxt }
    

    exportdata["tabs"][0]["contexts"][i]["testcases"].append( testcase )

write_json( exportdata )