import random


def szamlist(list):
    paros=[]
    for szam in list:
        if szam % 2 == 0:
            paros.append(szam)
    return paros

szamlista= []
#for i in range(10):
 #   szam = random.randint(0,10)
  #  szamlista.append(szam)
szam = input("add meg egy szamot")
while szam !='':
    szamlista.append(int(szam))
    szam = input("adj meg egy szamot")

print(szamlista)
print(szamlist(szamlista))







