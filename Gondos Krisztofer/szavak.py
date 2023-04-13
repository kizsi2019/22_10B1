szo_a = input('Adj meg egy szót! ')
szo_b = input('Adj meg egy másik szót! ')

len(szo_a)
len(szo_b)

if szo_a > szo_b:
    print(f'A hosszabb szó: {szo_a}')
elif szo_a == szo_b:
    print(A két szó egyforma hosszú.)
else:
    print('A második szó hosszabb.')