import random

def paros_e(list):
    paros = []
    for szam in list:
        if szam % 2 == 0:
            paros.append(szam)
    return paros

#szamlista = [1,2,3,4,5,6,7,8,9,10]

szamlista = []
#for i in range (10)
    #szam = random.randint(0,10)
    #szamlista.apend(szam)

szam = input("Adj meg egy számot!")
while szam !='':
    szamlista.append(int(szam))
    szam = input("Adj meg egy számot!")

print(paros_e(szamlista))
print(szamlista)
