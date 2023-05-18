import random

lista = []
szam = 0
talalat = False
index = 0

for i in range(5):
    szam = random.randint(1,7)
    lista.append(szam)

valasz = int(input("Adj meg 1 és 7 között egy számot! "))

while index < len(lista) and not talalat:
    if lista[index] - valasz == 0:
        talalat = True
    index = index + 1

if talalat:
    print('Van a listában ez a szám.')
else:
    print('Nincs a listában ez a szám.')
print(lista)
