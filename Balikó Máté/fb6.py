lista = [1,2,3,4,55,6,7,8,7,8,98,99,885,53]

max = lista[0]
min = lista[0]
for szam in lista:
    if szam > max:
        max = szam
    if szam < min:
        min = szam


osszeg= max - min
print("A lista legnagyobb száma: ",max)
print("A legkisebbszám a listában: ",min)

print("összege:", osszeg)