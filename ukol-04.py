class Auto:
    def __init__(self, registracka, typ, km):
        self.registracka = registracka
        self.typ = typ
        self.km = km
        self.stav = True

    def pujc_auto(self):
        if self.stav is True:
            self.stav == False
            return f"Potvrzuji zapůjčení vozidla."
        else:
            return f"Vozidlo není k dispozici."

    def get_info(self):
        return f"{self.typ} má registrační značku {self.registracka}."

Peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio",47534)
Škoda = Auto("1P3 4747", "Škoda Octavia",41253)

auto_k_pujceni = str(input("Přejete si půjčit Peugeot nebo Škoda?"))

if auto_k_pujceni == "Peugeot":
    print (Peugeot.get_info())
    print (Peugeot.pujc_auto())


if auto_k_pujceni == "Škoda":
    print (Škoda.get_info())
    print (Škoda.pujc_auto())


