def nagy(list):
    max = list[0]
    for szam in list:
        if szam > max:
            max = szam
    return max

lista = [1, 6, 3 ,6, 5]
print(nagy(lista))
