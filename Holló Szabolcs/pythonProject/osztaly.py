class TizB:
    def __init__(self, fiu, lany):
        self.fiu = fiu
        self.lany = lany

tizb_01 = TizB(29, 2)

with open('osztaly1.txt', 'w', encoding='utf-8') as celfajl:
    celfajl.write(f'A10B-be {tizb_01.fiu} fiú, és {tizb_01.lany} lány jar')
