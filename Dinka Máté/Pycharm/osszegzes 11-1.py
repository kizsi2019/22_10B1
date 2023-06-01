import random

lista = []
for i in range(5):
    szam = random.randint(1,10)
    lista.append(szam)
    if szam % 2 == 0:
        lista.append(szam)
osszeg = 0
for i in lista:
    osszeg = osszeg + i
    
print("A lista összege: ", osszeg)
print("A list elemei: ",lista)