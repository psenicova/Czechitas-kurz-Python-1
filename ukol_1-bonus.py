jmeno_a_prijmeni = input("Zadej jméno a příjmení: ")
jmeno, prijmeni = jmeno_a_prijmeni.split(" ")

#všechna písmena velká (vypíše např. JANA MALÁ)
print(f"{jmeno.upper()} {prijmeni.upper()}")

#všechna písmena malá (vypíše např. jana malá)
print(f"{jmeno.lower()} {prijmeni.lower()}")

#standardní varianta - první písmeno velké, další malá (vypíše např. Jana Malá)
print(f"{jmeno.strip()} {prijmeni.strip()}")

#iniciály (vypíše např. J. M.)
print(jmeno[0] + ". " + prijmeni[0] + ".")

#křestní jméno zkrácené na první písmeno a příjmení, pokud je křestní jméno delší než 5 znaků. Jinak vypíše standardní variantu, tj. první písmeno velké, další malá (u vstupu Jarmila Malá by došlo ke zkrácení křestního jména, zatímco u vstupu Jana Malá nikoliv)
if len(jmeno)>5:
    print(jmeno[0] + ". " + prijmeni)
else:
    print(jmeno_a_prijmeni)