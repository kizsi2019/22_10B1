def sikeres(pontszam):
    if pontszam >= 48:
        return True
    else:
        return False

nev = None

while nev != '':
    nev = input('Vizsgazo neve')
    if nev:
        pontszam = int(input('pontszam'))
        if sikeres(pontszam):
            print(nev,'ugyes vagy')
        else:
            print(nev,'buta vagy')