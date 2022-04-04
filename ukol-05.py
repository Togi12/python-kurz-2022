
class Polozka:
  def __init__(self, nazev, zanr):
    self.nazev = nazev
    self.zanr = zanr
  def __str__(self):
    return f"Žánr položky {self.nazev} je {self.zanr}."

class Film(Polozka):
  def __init__(self, nazev, zanr, delka):
    super().__init__(nazev, zanr)
    self.delka = delka
  def __str__(self):
    text = super().__str__()
    text = text + f" Délka filmu je: {self.delka}."
    return text

class Serial(Polozka):
  def __init__(self, nazev, zanr, pocet_epizod, delka_epizody):
    super().__init__(nazev, zanr)
    self.pocet_epizod = pocet_epizod
    self.delka_epizody = delka_epizody
  def __str__(self):
    text = super().__str__()
    text = text + f" Seriál má {self.pocet_epizod} epizod a délka epizody je: {self.delka_epizody}."
    return text

a=Film("a","komedie","91 minut")
b=Serial("b","drama",8, "40 minut")

print(a)
print(b)