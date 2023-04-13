szam = int(input("Addj meg egy számot -5 és 5 között! "))
szam_list = []

while szam >= -5 and szam <= 5:
    szam_list.append(szam)
    szam = int(input("Addj meg egy másik számot -5 és 5 között! "))

összeg = 0
for i in szam_list:
    összeg = összeg + i

print("A lista összege:", összeg)
print("A lista elemei:", szam_list)
