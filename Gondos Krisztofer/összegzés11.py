import random
'''
szam_v = 0
szam_list = []
for i in range(5):
    szam_v = random.randint(1,10)
    szam_list.append(szam_v)
összeg = 0
for i in szam_list:
    összeg = összeg + i
print(összeg)
print(szam_list)
'''

szam_v = 0
szam_list = []
for i in range(5):
    szam_v = random.randint(1,10)
    if szam_v % 2 == 0:
        szam_list.append(szam_v)
összeg = 0
for i in szam_list:
    összeg = összeg + i
print("A lista összege:", összeg)
print("A lista elemei:", szam_list)
