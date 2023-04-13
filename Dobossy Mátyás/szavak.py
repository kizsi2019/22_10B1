szo = input("Adj meg egy szót! ")
szo2 = input("Adj meg egy másik szót! ")

if len(szo) > len(szo2):
    print("A hosszabb szó: ", szo)
elif len(szo) == len(szo2):
    print("A két szó egyforma hosszú.")
elif len(szo) < len(szo2):
    print("A hosszabb szó: ", szo2)