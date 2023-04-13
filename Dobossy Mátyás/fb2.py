def Legnagyobb(list):
    legnagyobb = 0
    list.sort()

    for i in list:
        if list[0] <= i:
            legnagyobb = i

    return legnagyobb

szam = input("Adj meg egy számot: ")
listaaa = []
while szam != '':
    listaaa.append(int(szam))
    szam = input("Adj meg egy számot: ")

print(Legnagyobb(listaaa))