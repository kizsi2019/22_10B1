import datetime

class Diak:
    def __init__(self, nev, osztaly, szuletesi_ev):
        self.nev = nev
        self.osztaly = osztaly
        self.szuletesi_ev = szuletesi_ev

    def kor(self):
        return datetime.datetime.now().year - self.szuletesi_ev

    def info(self):
        print(f"Szia, {self.nev} vagyok, a {self.osztaly} osztályba járok, {self.kor()} vagyok")


diak1 = Diak("Kiss Péter", "10. A", 2006)

print(diak1.info())