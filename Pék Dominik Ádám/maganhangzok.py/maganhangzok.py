def maganhangzok(mondat):
    maganhangzok = ['a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'ö', 'ő', 'u', 'ú', 'ü', 'ű']
    maganhangzoszam = 0

    for i in mondat:
        if i.lower() in maganhangzok:
            maganhangzoszam += 1

    return maganhangzoszam

mondat = input("Adjon meg egy szöveget: ")
maganhangzoszam = maganhangzok(mondat)
print("A szövegben", maganhangzoszam, "magánhangzótalálható.")
