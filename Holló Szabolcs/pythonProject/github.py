def vlami(list):
    min = list[0]
    for szam in list:
        if szam < min:
            min = szam
    return min

lista = [1, 6, 3 ,6, 5]
print(vlami(lista))
