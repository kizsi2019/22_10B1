lmao2 = input("Adja meg a szoveget:")



def countmaganhangzo(lmao):
    maganhangzo = ('a, á, e, é, i, í, o, ó, ö, ő, u, ú, ü, ű')
    maganhangzo_kek = 0



    for char in lmao:
        if char.lower() in maganhangzo:
            maganhangzo_kek += 1

    return maganhangzo_kek



maganhangzo_kek = countmaganhangzo(lmao2)

print("Ebben a szovegben", maganhangzo_kek, "maganhangzo van")