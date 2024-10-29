studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]
meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]
tavi = ["tava"] * 7 
istoric_comenzi = []
nr_ceafa=meniu.count("ceafa")
nr_ceafa_comandata=comenzi.count("ceafa")
ceafa_disponibila=nr_ceafa-nr_ceafa_comandata
nr_papanasi=meniu.count("papanasi")
nr_papanasi_comandati=comenzi.count("papanasi")
nr_papanasi_disponibili=nr_papanasi-nr_papanasi_comandati
print(nr_papanasi_disponibili)
nr_guias=meniu.count("guias")
nr_guias_comandat=comenzi.count("guias")
nr_guias_disponibil=nr_guias-nr_guias_comandat
pret_guias=preturi[2][1]
pret_papanasi=preturi[0][1]
pret_ceafa=preturi[1][1]
incasare_cantina=nr_papanasi_comandati*pret_papanasi+nr_guias_comandat*pret_guias+nr_ceafa_comandata*pret_ceafa
while studenti:
    client=studenti.pop(0)
    comanda1=comenzi.pop(0)
    tavi.pop(0)
    print(f"studentul {client} a comandat {comanda1}")
    istoric_comenzi.append(f"{client} a comandat {comanda1}")

nr_tavi_ramase=tavi.count("tava")
print(f"S-au comandat {nr_ceafa_comandata} portii de ceafa")
print(f"S-au comandat {nr_papanasi_comandati} portii de papanasi")
print(f"S-au comandat {nr_guias_comandat} portii de guias") 
print(f"Au ramas {nr_tavi_ramase} tavi")
if ceafa_disponibila>0:
    print("true")
else:
    print("false")
if  nr_papanasi_disponibili>0:
    print("true")       
else:
    print("false")
if nr_guias_disponibil>0:
    print("true")
else:
    print("false")
print(f"Cantina a incasat azi {incasare_cantina} de lei")      
    
                


