import json

with open('body.json', encoding='utf-8') as file:
    body = json.load(file)

import json

with open('bonusy.json', encoding='utf-8') as file:
    bonusy = json.load(file)

print(body.items())
print(bonusy.items())

body_celkem = {}

for bod in body:
    vysledne_body = body[bod]
    #print(vysledne_body)

for bonus in bonusy:
    vysledne_bonusy = bonusy[bonus]
    #print(vysledne_bonusy)

body_celkem = vysledne_body + vysledne_bonusy

for jmeno, pocet_bodu in body_celkem.items():

    if pocet_bodu >= 90:
        body_celkem[jmeno] = 1
    elif pocet_bodu >= 70:
        body_celkem[jmeno] = 2
    elif pocet_bodu >= 50:
        body_celkem[jmeno] = 3
    elif pocet_bodu >= 30:
        body_celkem[jmeno] = 4
    else:
        body_celkem[jmeno] = 5


with open('znamky.json', mode='w', encoding='utf-8') as file:
    json.dump(body_celkem, file, ensure_ascii=False)