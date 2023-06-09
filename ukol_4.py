tel_cislo_s_mezerami = input("Zadej telefonní číslo: ")
tel_cislo = tel_cislo_s_mezerami.replace(" ","")

def over_telefon(tel_cislo: str) -> bool: #ikdyž vkládáme telefonní číslo, jedná se vlastně o str, nikoliv o int
    """
    Funkce ověřuje zadané telefonní číslo, jestli splňuje podmínky na délku čísla a předvolbu.
    """
    predvolba = tel_cislo[0:4]
    if predvolba == "+420" and len(tel_cislo) == 13:
        return True
    elif len(tel_cislo) == 9:
        return True
    else:
        return False
    
    #funkce by šla napsat i takto:

    # if predvolba == "+420" and len(tel_cislo) == 13:
    #     return True
    # if len(tel_cislo) == 9:
    #     return True
    # return False

overeni_cisla = over_telefon(tel_cislo)
# print(overeni_cisla) <--- pro případnou kontrolu

if overeni_cisla == False: #od Kačky: lepší je if not overeni_cisla
     print("Chybně zadané telefonní číslo!")
     exit()
else:
    zprava = input("Zadej text zprávy: ")

import math #dává se na začátek souboru

def cena_zpravy(zprava: str) -> int:
    """
    Funkce vypočítává cenu za zprávu podle podmínky, že za každých započatých 180 znaků zákazník zaplatí 3 Kč.
    """
    cena_za_180_znaku = 3
    pocet_znaku = len(zprava)
    return math.ceil(pocet_znaku / 180) * cena_za_180_znaku

overeni_ceny = cena_zpravy(zprava)
print(f'Zpráva tě bude stát {overeni_ceny} Kč.')