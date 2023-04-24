import json

with open('body.json', encoding='utf-8') as file:
    body = json.load(file)

with open('bonusy.json', encoding='utf-8') as file:
    bonusy = json.load(file)

prospech = {}

for jmeno, pocet_bodu in body.items():
    prospech[jmeno] = "Fail"

    if pocet_bodu > 60:
        prospech[jmeno] = "Pass"


for jmeno, bonus in bonusy.items():
    if jmeno in body:
        body[jmeno] = body[jmeno] + bonus

for jmeno, pocet_bodu in body.items():
    if pocet_bodu >= 90:
        body[jmeno] = 1
    elif pocet_bodu >= 70:
        body[jmeno] = 2
    elif pocet_bodu >= 50:
        body[jmeno] = 3
    elif pocet_bodu >= 30:
        body[jmeno] = 4
    else:
        body[jmeno] = 5

with open('znamky.json', mode='w', encoding='utf-8') as file:
    json.dump(body, file, ensure_ascii=False)

with open('prospech.json', mode='w', encoding='utf-8') as file:
    json.dump(prospech, file, ensure_ascii=False)