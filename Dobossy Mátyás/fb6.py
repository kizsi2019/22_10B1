def Kulonbseg(list):
    list.sort
    return int(list[0]) - int(list[len(list) - 1])

szam = input("Adj meg egy számot: ")
listaaa = []
while szam != '':
    listaaa.append(int(szam))
    szam = input("Adj meg egy számot: ")

print(Kulonbseg(listaaa))