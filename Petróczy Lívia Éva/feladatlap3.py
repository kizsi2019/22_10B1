def nagyobb_e(list):

    for szam in list:
        if szam > max:
            max = szam
    return nagyobb

lista = []
szam = input("Adj meg egy számot! ")
while szam !='':
    lista.append(int(szam))
    szam = input("Adj meg egy számot! ")
print(lista)
print(nagyobb(lista))

