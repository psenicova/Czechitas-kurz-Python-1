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

print(hodnoceni)
print(nove_hodnoceni)

with open('prospech.json', mode='w', encoding='utf-8') as file:
    json.dump(nove_hodnoceni, file, ensure_ascii=False)

