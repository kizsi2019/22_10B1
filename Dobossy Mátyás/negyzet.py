class Negyzet:
    def __init__(self, hossz):
        self.hossz = hossz

    def terulet(self):
        return self.hossz * self.hossz

    def kerulet(self):
        return self.hossz * 4

    def info(self):
        print(f"A(z) {self.hossz} hosszúsagú négyzet kerülete: {self.kerulet()}, területe: {self.terulet()}")


negyzet1 = Negyzet(10)

print(negyzet1.terulet())
print(negyzet1.kerulet())
print(negyzet1.info())