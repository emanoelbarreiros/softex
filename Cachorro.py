class Cachorro:

    incremento = 0

    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento

    def __str__(self):
        return "{}, {}".format(self.nome, self.nascimento)

    def incrementar():
        Cachorro.incremento += 1

c = Cachorro("Bob", "12/03/2015")
c2 = Cachorro("Max", "10/10/2020")

print(c)
print(c2)

Cachorro.incrementar()

print(c.incremento)
print(c2.incremento)

Cachorro.incrementar()

print(c.incremento)
print(c2.incremento)