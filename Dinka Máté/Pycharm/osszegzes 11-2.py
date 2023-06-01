lista = []
szam = int(input("Adj meg egy egész számot [-5;5] között: "))
while szam >= -5 and szam <= 5:
    lista.append(szam)
    szam = int(input("Adj meg egy egész számot [-5;5] között: "))

összeg = 0

for i in lista:
    összeg = összeg + i

print("A lista összege: ", összeg)
print("A list elemei: ",lista)
