
#kibaszott idiota

#input("Add meg a vizsgázó nevét!")
#a1 = int(input('Adja meg a pontszámát'))

#if a1 > 48:
#    print('Sikeres vizsga')
#else:
#    print('Nem ment át')


nev = input('add meg a nevet')
pontszam = input("Add meg a pontszámod: ")

def sikeres(pontszam):
    if pontszam>=48:
        return True
    else:
        return False

nev = None
nev = input('add meg a nevet')

while nev !="":
    nev = input('add meg a nevet')
    if nev:
        pontszam = int(input('Add meg a pontszamot'))
        if sikeres(pontszam):
            print(nev,' vizsgaja sikeres')
        else:
            print(nev,'vizsgaja sikertelen')