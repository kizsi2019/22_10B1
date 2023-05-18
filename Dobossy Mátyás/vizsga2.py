nev = input("Add meg a vizsgázó nevét: ")
while nev != "":
    pontszam  = int(input("Add meg a pontszámát: "))

def test(sikeres):
    while nev != "" and pontszam != "":
        if pontszam >= 48:
            return True
        else:
            return False


if test(True) and nev != "" and pontszam != "":
    print(nev, "átment a vizsgán")
if test(False) and nev != "" and pontszam != "":
    print(nev, "nem ment át a vizsgán")