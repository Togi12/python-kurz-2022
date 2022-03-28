
def phone_number (cislo:str):
    if len(cislo)==13:
        return True
    if len(cislo)==9:
        return True
    else:
        return False

zadane_cislo = int(input("Zadej číslo, kam chceš zaslat zprávu: "))

cislo=str(zadane_cislo)

spravnost_cisla = phone_number (cislo)

print (spravnost_cisla)

if spravnost_cisla is False:
    print("Zadané číslo neexistuje.")

if spravnost_cisla is True:
    zprava = int(input("Zadej zprávu, kterou chceš odeslat: "))

def cena():
    return ceil(len(int(zprava))/180*3)