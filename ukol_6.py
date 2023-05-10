import re

uzivatelske_jmeno = input("Zadej uživatelské jméno: ")

regularni_vyraz = re.compile(r"[a-zA-Z]{6,10}")

kontrola_jmena = regularni_vyraz.fullmatch(uzivatelske_jmeno)

if kontrola_jmena:
    heslo = input("Zadej heslo: ")

else:
    print("Zadané uživatelské jméno nesplňuje podmínky.")
    exit()

regularni_vyraz2 = re.compile(r"[\w\-.+=]{12,30}")

kontrola_hesla = regularni_vyraz2.fullmatch(heslo)

if kontrola_hesla:
    email = input("Zadej e-mailovou adresu: ")
else:
    print("Zadané heslo nesplňuje podmínky.")
    exit()

regularni_vyraz3 = re.compile(r"\w+(\.\w+)?@\S+.[a-z]*")

kontrola_emailu = regularni_vyraz3.fullmatch(email)

if kontrola_emailu:
    print("Můžeš vstoupit.")
else:
    print("Zadaný e-mail nesplňuje podmínky.")
    exit()