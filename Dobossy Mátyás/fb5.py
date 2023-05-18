def ParosSzamok(list):
    parosak = []

    for i in list:
        if i % 2 == 0:
            parosak.append(i)

    return parosak

szam = input("Adj meg egy számot: ")
listaaa = []
while szam != '':
    listaaa.append(int(szam))
    szam = input("Adj meg egy számot: ")

print(ParosSzamok(listaaa))