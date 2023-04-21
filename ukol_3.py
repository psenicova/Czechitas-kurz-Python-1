import json

with open('body.json', encoding='utf-8') as file:
    hodnoceni = json.load(file)

nove_hodnoceni = {}
print(hodnoceni.items())
for jmeno, body in hodnoceni.items():
    if body >= 60:
        nove_hodnoceni[jmeno] = "Pass"
    else:
        nove_hodnoceni[jmeno] = "Fail"

print(hodnoceni) # jen pro kontrolu
print(nove_hodnoceni) # jen pro kontrolu

with open('prospech.json', mode='w', encoding='utf-8') as file:
    json.dump(nove_hodnoceni, file, ensure_ascii=False)

