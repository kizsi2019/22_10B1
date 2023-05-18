'''
for Oszt in range(3,40,3):
    print(Oszt)
'''
'''
szamd = 1
while szamd <= 40:
    if szamd % 3 == 0:
        print(szamd)
    szamd = szamd + 1
'''
tantargyak = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']
T_szo = []

for szo in tantargyak:
    if szo[0] == "T":
        T_szo.append(szo)
    if szo[0] == "t":
        T_szo.append(szo)

print(T_szo)

szamok = [120, 9, 5, 24, 6, 17, -45, 92, 15, 48, 57]

for szam in szamok:
    if szam % 3 == 0:
        print(szam)
