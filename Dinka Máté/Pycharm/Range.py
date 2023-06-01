
#kiírja a páros számokat 1 és 10 között

for szam in range(0,12, 2):
 print(szam)
#csökkenő sorrendben írja ki a számokat 1 és 10 között

for szam in range(10,0, -1):
    print(szam)
#kiírja a páratlan számokat csökkenő sorrendben 1 és 10 között

for szam in range(10, 0, -1):
    if szam%2:
     print(szam)

#amely kiírja a páros számokat a 2 jegyű számok közül és, amelyek oszthatók 7-el.

for szam in range(10,99, 2):
 print(szam)
 if szam%%7:
  print(szam)

#Írj egy programot ami generál egy véletlen számot 100 és 500 között, majd majd a generált számig számoljuk meg hány db 6 osztható szám van.

import random
szam = random.randint(100,500)
print (szam%6)

#Kamat
import math

szam = 500000

round(szam, -3)
