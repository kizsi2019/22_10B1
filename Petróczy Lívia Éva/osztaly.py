class Tiz_b:

    def __init__(self, fiu, lany):
        self.fiu = fiu
        self.lany = lany


tiz_b_01 = Tiz_b(29,2)


with open('osztaly.txt', 'w', encoding='utf-8') as celfajl:
    celfajl.write(f'A 10.B osztályba {tiz_b_01.fiu} fiú és {tiz_b_01.lany} lány jár.')
