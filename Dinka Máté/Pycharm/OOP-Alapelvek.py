class Diak:
    def __init__(self, nev, osztaly):
        self.nev = nev
        self.osztaly = osztaly

    def info(self):
        print(f'Szia, {self.nev} vagyok, {self.osztaly} osztályba járok. ')

class Tanar:
    def __init__(self, nev, szak):
        self.nev = nev
        self.szak = szak

    def info(self):
        print(f'Szia, {self.nev} vagyok, {self.szak} szakos tanár vagyok. ')


diak_01 = Diak('Kiss Péter', '10A')
tanar_01 = Tanar('Kiss Zsigmond', 'Informatikus')
tanar_02 = Tanar('Nagy józsef', 'testnevelés')

diak_01.info()
tanar_01.info()
tanar_02.info()

print(tanar_02.nev)
print(diak_01.osztaly)

