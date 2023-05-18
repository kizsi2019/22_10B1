class TizB:
    def __init__(self, fiu, lany):
        self.fiu = fiu
        self.lany = lany



_tizB = TizB(29, 2)

with open('./osztaly.txt', 'w', encoding='utf-8') as fajl:
    fajl.write(f"Az osztályba {_tizB.fiu} fiú és {_tizB.lany} lány jár")