import random
lista = []

for i in range(5):
    szam = random.randint(1,7)
    lista.append(szam)

szam2 = int(input("Adj meg egy számot: "))

talalat = False
index = 0

while index < len(lista) and talalat:
    if lista[index] == szam2:
        talalat = True

if talalat:
    print('Van a listában hárommal osztható szám.')
else:
    print('Nincs a listában hárommal osztható szám.')

print(lista)
