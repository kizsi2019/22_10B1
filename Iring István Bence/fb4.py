
def atlag(lista):
    osszeg = 0
    for szam in lista:
        osszeg += szam
    return osszeg/len(lista)
szamlista = [1,2,3,4,5,6,7,8,]
print(atlag(szamlista))
