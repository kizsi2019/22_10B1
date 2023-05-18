def nagyobb(list):
    max = list[0]
    for szam in list:
        if szam > max:
            max = szam
    return max

lista = []
szam = input("Adj meg egy számot!")
while szam !='':
    lista.append(int(szam))
    szam = input("Adj meg egy számot!")

print(lista)
print(nagyobb(list))
