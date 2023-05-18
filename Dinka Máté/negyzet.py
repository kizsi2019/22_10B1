class Negyzet:
    def __init__(self, hossz):
        self.hossz = hossz
    def terulet(self):
        return self.hossz * self.hossz
    def kerulet(self):
        return self.hossz * 4
    def info(self):
        print(f'A(Z) {self.hossz} oldalú négyzet kerülete {self.kerulet() }, területe: {self.terulet() }')

negyzet_01 = Negyzet(8)
#print(negyzet_01.terulet())
negyzet_01.info()