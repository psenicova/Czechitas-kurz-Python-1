teploty = [
    ["pondělí", 2.1, 5.2, 6.1, -0.1],
    ["úterý", 2.2, 4.8, 5.6, -1.0],
    ["středa", 3.3, 6.5, 5.9, 1.2],
    ["čtvrtek", 2.9, 5.6, 6.0, 0.0],
    ["pátek", 2.0, 4.6, 5.5, -1.2],
    ["sobota", 1.0, 3.2, 2.1, -2.0],
    ["neděle", 0.4, 2.7, 1.3, -2.8]
]

#Pomocí dict comprehension vytvoř slovník, který bude mít následující formát, kde klíčem bude den v týdnu, a hodnotou průměrná teplota ten den.
#{den: průměrná teplota}

for dny in teploty:
    den = dny[0]
    teplota1 = dny[1]
    teplota2 = dny[2]
    teplota3 = dny[3]
    teplota4 = dny[4]
    prumerna_teplota = round((teplota1 + teplota2 + teplota3 + teplota4) / 4,1) #jak dosadit 4 počtem teplot v jednotlivých dnech?
    print(den)
    print(prumerna_teplota)

prumerne_teploty = {}
prumerne_teploty = [den, prumerna_teplota]
print(prumerne_teploty)

# prumerne_teploty = {}
# prumerne_teploty = {den: str(prumerna_teplota) for den, prumerna_teplota in teploty.items()}
# print(prumerne_teploty)

#prumerne_teploty = {[sum(teplota) / len(teplota)] for den, teplota in teploty.items()}
#print(prumerne_teploty)
#prumerne_teploty = {den: sum(teplota) / len(teplota) for den, teplota in teploty.items()}
#print(prumerne_teploty)