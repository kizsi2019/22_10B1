class Diak:
    def __init__(self, nev, osztaly, ev):
        self.nev = nev
        self.osztaly = osztaly
        self.ev = ev

    def info(self):
        print(f"A diák neve: {self.nev} és a {self.osztaly} ba járok, ")


class Tanar:
    def __init__(self, nev, szak):
        self.nev = nev
        self.szak = szak

    def info(self):
        print(f"A tanár neve: {self.nev} és a {self.szak} ba járok")


diak01 = Diak("Kiss Péter", "10.B")
tanar01 = Diak("Horváth Zita", "Biológia")

print(diak01.osztaly)
print(tanar01.nev)