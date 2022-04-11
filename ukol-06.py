
with open('auta.txt', encoding='utf-8') as vstup:
    radky = vstup.readlines()

radky = [radek.split(' ') for radek in radky]

radky = [radek[1] for radek in radky]

radky = [radek.replace(",",".") for radek in radky]

radky = [radek.split('\n') for radek in radky]

radky = [radek[0] for radek in radky]

radky = [float(radek) for radek in radky]

print(radky)