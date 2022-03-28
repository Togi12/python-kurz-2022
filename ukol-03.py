"""
První funkce ověří délku telefonního čísla.
Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420").
Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili.
Pokud je číslo platné, funkce vrátí hodnotu True, jinak vrátí hodnotu False.
"""

def phone_number (tel_cislo:str):
    if len(tel_cislo)==13 or 9:
        return True
    else:
        return False

print(phone_number("++"))

tel_cislo = int(input("Zadej číslo, kam chceš zprávu zaslat: "))
mark = get_mark(points)
if mark == 5:
  points = int(input("Zadej počet bodů v opravném pokusu: "))
  mark = get_mark(points)
print(f"Výsledná známka je {mark}.")
