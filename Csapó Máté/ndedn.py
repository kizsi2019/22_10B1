nev=("")
pontszam=("")
while nev==(""):
      nev= input("add meg a neved: ")

while pontszam==(""):
      pontszam = int(input(("add meg a pontszámoz: ")))

def teszt(sikeres):
    if pontszam>=48:
        return True
    else:
        return False

if teszt(True):
    print(nev,'vizsgája sikeres')
else:
    print(nev,'vizsgája szikertelen')