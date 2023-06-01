Pontszam = int(input("Adjon meg egy pontszámot 0-100 között: "))

if 0 < Pontszam < 40:
    print("1. Érdemelsz")
elif 40 < Pontszam < 55:
    print("2. Érdemelsz")
elif 55 < Pontszam < 70:
    print("3. Érdemelsz")
elif 70 < Pontszam < 80:
    print("4. Édemelsz")
elif 80 < Pontszam < 100:
    print("5. Érdemelsz")
else:
    print("Hibás adatokat adtál meg!")