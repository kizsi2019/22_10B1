def Atlag(list):
    ossz = 0

    for i in list:
        ossz += i

    atlag = ossz / len(list)

    ind = []
    for i in list:
        if i > atlag:
            ind.append(list.index(i))

    return ind

szam = input("Adj meg egy számot: ")
listaaa = []
while szam != '':
    listaaa.append(int(szam))
    szam = input("Adj meg egy számot: ")

print(Atlag(listaaa))