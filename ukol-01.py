baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

kod_baliku = input("Jaky je kod vaseho baliku? ")

for kod_baliku in baliky:
    if baliky[kod_baliku, True]:
        print("Balík byl předán kurýrovi.")