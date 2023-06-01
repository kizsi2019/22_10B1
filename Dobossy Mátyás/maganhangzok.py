szoveg = input("Adj meg egy szöveget: ")

def Maganhangzo(szvg):
    szam = 0
    maganhangzok = ["e", "u", "i", "o", "ő", "ú", "ö", "ü", "ó", "a", "é", "á", "ű", "í"]

    szvg.lower()
    for i in maganhangzok:
        szam += szvg.count(i)
    return szam

print(f"A szövegben {Maganhangzo(szoveg)} magánhangzó található")