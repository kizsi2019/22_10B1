def maganhangzok(szoveg):
    maganhangzok_mennyisege = 0
    maganhangzok = "aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ"

    for betu in szoveg:
        if betu in maganhangzok:
            maganhangzok_mennyisege += 1

    return maganhangzok_mennyisege

mondat = input("Írjon egy mondatot!: ")

maganhangzok_mennyisege = maganhangzok(mondat)

print("A szövegben", maganhangzok_mennyisege, "magánhangzó található.")

