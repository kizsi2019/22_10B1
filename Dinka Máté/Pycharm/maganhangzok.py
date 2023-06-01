def maganhangzok(szoveg):
    maganhangzok_szama = 0
    maganhangzok = "aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ"

    for betu in szoveg:
        if betu in maganhangzok:
            maganhangzok_szama += 1

    return maganhangzok_szama

szoveg = input("Adjon meg egy szöveget: ")

maganhangzok_szama = maganhangzok(szoveg)

print("A szövegben", maganhangzok_szama, "magánhangzó található.")
