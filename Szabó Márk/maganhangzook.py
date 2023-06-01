def maganhangzok():
    szoveg = input("Adjon meg egy szöveget:")
    karakter = 'a,e,é,á,ű,ú,ő,ó,ü,ö,u,i,í,Á'
    darab = 0
    for char in szoveg:
        if char in karakter:
            darab += 1
    return darab

szam = maganhangzok()
print("A magánhangzók száma:", szam)




