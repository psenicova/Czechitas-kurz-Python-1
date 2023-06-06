class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True

    def pujc_auto(self):
        if self.dostupne:
            self.dostupne = False
            return "Potvrzuji zapůjčení vozidla"
        else:
            return "Vozidlo není k dispozici"
    
    def get_info(self):
        return f"Poptávané vozidlo má SPZ {self.registracni_znacka} a jedná se o {self.typ_vozidla}."

    def vrat_auto(self, stav_tachometru, dny_vypujcky):
        self.stav_tachometru = stav_tachometru
        self.dny_vypujcky = dny_vypujcky
        if not self.dostupne:
            self.dostupne = True




auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253)

vozidlo = input("Jaké vozidlo si přejete půjčit?")

if vozidlo == "Peugeot":
    print(auto1.get_info())
    print(auto1.pujc_auto())
    print(auto1.pujc_auto())
    print(auto1.vrat_auto())
    print(auto1.pujc_auto())
elif vozidlo == "Škoda":
    print(auto2.get_info())
    print(auto2.pujc_auto())
    print(auto2.pujc_auto())
else:
    print("Požadované auto nemáme k dispozici")