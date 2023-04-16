#Vyvíjíš software pro obchod s elektronickými součástkami. Firma eviduje informace o počtu součástek na skladě ve slovníku. Klíč slovníku je kód součástky a hodnota klíče je počet součástek na skladě.

sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

print(sklad.items())

kod_soucastky = input("Zadej kód součástky: ")
if kod_soucastky not in sklad:
    print("Součástka není skladem.")
else:
    pocet_soucastek = int(input("Zadej počet požadovaných kusů: "))
    if pocet_soucastek > sklad[kod_soucastky]:
        print(f'Lze prodat pouze omezené množství {sklad[kod_soucastky]} kusů.')
        sklad.pop(kod_soucastky) #součástku odeber ze slovníku, protože je vyprodaná
        print(sklad)
    else:
        print(f'Poptávku lze uspokojit v plné výši')
        sklad[kod_soucastky] -= pocet_soucastek #sniž počet součástek na skladě o množství požadované zákazníkem
        print(sklad[kod_soucastky])