# 1. Lista de cuvinte și alegerea cuvântului la întâmplare
import random
from dataclasses import replace

cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]
print("Let's play a little game")
# 2. Inițializarea numărului de încercări   
incercari_ramase = 6
litere_incercate = []
# 3.introducerea caracterului
lung_cuv=len(cuvant_de_ghicit)
#bucla
while incercari_ramase>0:
    lit=input()
    z=lit.isalpha()
    # conditii litera
    if (lit not in cuvant_de_ghicit and lit not in litere_incercate):
        incercari_ramase = incercari_ramase - 1
    if(lit not in litere_incercate):
        litere_incercate.append(lit)
    else:
        print("aceasta litera a fost zisa")
    if(len(lit)>1):
        print("doar un caracter")
    if(z==False):
        print("doar caractere")
        #gasirea literei in cuvant si inlocuirea pe aceleasi pozitii in progres
    for i in range(len(cuvant_de_ghicit)) :
        if(cuvant_de_ghicit[i]==lit):
            progres[i]=lit
    print(f" mai ai {incercari_ramase} incercari")
    print(progres)
    print(litere_incercate)
    if("_" not in progres):
        print("Felicitari ai ghicit cuvantul")
        break
if(incercari_ramase==0):
    print(f"Ai pierdut,cuvantul era {cuvant_de_ghicit}")
