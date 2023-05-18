def Atlag(list):
    ossz = 0

    for i in list:
        ossz += i

    return ossz / len(list)

szam = input("Adj meg egy számot: ")
listaaa = []
while szam != '':
    listaaa.append(int(szam))
    szam = input("Adj meg egy számot: ")

print(Atlag(listaaa))