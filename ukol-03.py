
def phone_number (cislo:str):
    if len(cislo)==13:
        return True
    if len(cislo)==9:
        return True
    else:
        return False

cislo = str(input("Zadej číslo, kam chceš zaslat zprávu: "))

spravnost_cisla = phone_number (cislo)

print (spravnost_cisla)

if spravnost_cisla is False:
    print("Zadané číslo neexistuje.")

if spravnost_cisla is True:
    zprava = str(input("Zadej zprávu, kterou chceš odeslat: "))


def cena():
    return cena_zpravy

cena_zpravy=round(len(zprava)/180*3)

print("Cena zprávy je:")
print(cena())