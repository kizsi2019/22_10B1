class Tizb:
    def __init__(self, fiu, lany):
        self.fiu = lany
        self.lany = lany


tizB_01 = Tizb(29,2)

with open('osztaly.txt', 'w', encoding='utf-8') as celfajl:
    celfajl.write(f'A 10B-be {tizB_01.fiu} fiu es {tizB_01.lany} lany jar')





