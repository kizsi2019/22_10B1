lista = [12, 5, 4, 8, 9, 11, 10, 12, 6]

k = 0

min = lista[0]
max = lista[0]
for szam in lista:
    if szam < min:
        min = szam
    if szam > max:
        max = szam

k = max - min

print(k)
