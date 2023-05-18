def sikeres(pontszam):
    if pontszam >= 120:
        return True
    else:
        return False

nev = None

while nev != '':
    nev = input('Add meg a nevét! ')
    if nev:
        pontszam = int(input('Add meg a pontszámát! '))
        if sikeres(pontszam):
            print(nev, 'vizsgája sikeres.')
        else:
            print(nev, 'vizsgája sikertelen:')