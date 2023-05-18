class Negyzet:
    def __init__ (self, hossz):
        self.hossz =hossz
    def terulet(self):
        return self.hossz * self.hossz
    def kerulet(self):
        return  self.hossz * 4
    def info(self):
        print(f'A(z) {self.hossz} cm hosszú oldalú négyzet kerülete: {self.kerulet()} cm, területe: {self.terulet()} cm2.')

negyzet_1 = Negyzet(10)
#print(negyzet_1.terulet())
negyzet_1.info()
