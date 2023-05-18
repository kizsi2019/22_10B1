'''
def nagyobb(list):
    nagyobb =[]
    for szam in list:
        if szam % 2 == 0:
            nagyobb.append(szam)
    return nagyobb
lista = [1,2,3,4,5,6,7,8,9,10]
max = lista[0]
for szam in lista:
    if szam > max:
        max = szam
print("Legnagyobb szám: ", max) #3
'''
'''
def szavak_szama(szoveg):
    szavak = szoveg.split()
    return len(szavak)
mondat = "Ez egy példa mondat."
szavak = szavak_szama(mondat)
print(szavak) # 4
'''
