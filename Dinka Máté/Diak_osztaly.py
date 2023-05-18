import datetime

class Diak:

    def __int__ (self, nev, osztaly, szuletesi_ev,):
        self.nev = nev
        self.osztaly = osztaly
        self.szuletesi_ev = szuletesi_ev

    def eletkor(self):
        return datetime.datetime.now().year - self.szuletesi_ev

    def info(self):
        print(f'Szia, {self.nev} vagyok, {self.osztaly} osztályba járok, {self.szuletesi_ev} éves vagyok.')

diak_01 = Diak('Kiss Péter', '10.B', 2008)
diak_01.info()