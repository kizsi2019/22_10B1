nyers_szoveg = input("Adjon meg egy szöveget: ")


def maganhangzok(szoveg):
    osz_maganhangzok = "aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ"
    szam = 0
    for betu in szoveg:
        if betu in osz_maganhangzok:
            szam += 1
    return szam

maganhangzok_01 = maganhangzok(nyers_szoveg)
print(f'A szövegben {maganhangzok_01} magánhangzó található.')
