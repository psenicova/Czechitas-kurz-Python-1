import json

with open('body.json', encoding='utf-8') as file:
    hodnoceni = json.load(file)

import json

print(hodnoceni.items())
for jmeno, body in hodnoceni.items():
    if body >= 60:
        hodnoceni[jmeno] = "Pass"
    else:
        hodnoceni[jmeno] = "Fail"

with open('prospech.json', mode='w', encoding='utf-8') as file:
    json.dump(hodnoceni, file, ensure_ascii=False)