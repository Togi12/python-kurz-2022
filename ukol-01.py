baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

kod_baliku = input("Jaky je kod vaseho baliku?")

if baliky[kod_baliku] is True:
    print("Balík byl předán kurýrovi.")
if baliky[kod_baliku] is False:
    print("Balík zatím nebyl předán kurýrovi.")