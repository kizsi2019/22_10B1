def Fordit(list):
    list.reverse()
    return list

szam = input("Adj meg egy számot: ")
listaaa = []
while szam != '':
    listaaa.append(int(szam))
    szam = input("Adj meg egy számot: ")

print(Fordit(listaaa))