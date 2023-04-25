tel_cislo = (input("Zadej telefonní číslo: "))

def over_cislo(tel_cislo):
    ma_predvolbu = tel_cislo.startswith('+420')
    delka = len(tel_cislo)
    if (ma_predvolbu and delka == 13) or delka == 9:
        return True
    else:
        return False
    
    # zkrácená verze:
    # def over_cislo(tel_cislo):
    # ma_predvolbu = tel_cislo.startswith('+420')
    # delka = len(tel_cislo)
    # return((ma_predvolbu and delka == 13) or delka == 9)
    
overeni = over_cislo(tel_cislo)
print(overeni)