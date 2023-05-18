class Diak:

    def __init__(self, nev, osztaly):
        self.nev = nev
        self.osztaly = osztaly
    def info(self):
        print(f'Szia a nevem {self.nev}, és a(z) {self.osztaly} osztályba járok. ')

class Tanar:

    def __init__(self, nev, szak):
        self.nev = nev
        self.szak = szak
    def info(self):
        print(f'Szia a nevem {self.nev}, és a(z) {self.szak} szakos tanár vagyok. ')

diak_01 = Diak('Kiss Péter', '10A')
tanar_01 = Tanar('Horváth Zita', 'biológia-kémia')

diak_01.info()
tanar_01.info()
