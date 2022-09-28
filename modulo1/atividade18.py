class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def __str__(self):
        return f"{self.nome}, {self.idade}, {self.cpf}"

class Complexo:
    def __init__(self, real, imaginaria):
        self.real = real
        self.imaginaria = imaginaria

    def __add__(self, n):
        novoReal = self.real + n.real
        novoImaginaria = self.imaginaria + n.imaginaria
        return Complexo(novoReal, novoImaginaria)

    def __sub__(self, n):
        novoReal = self.real - n.real
        novoImaginaria = self.imaginaria - n.imaginaria
        return Complexo(novoReal, novoImaginaria)

    def __mul__(self, n):
        novoReal = self.real*n.real - self.imaginaria*n.imaginaria
        novoImaginaria = self.real*n.imaginaria + self.imaginaria*n.real
        return Complexo(novoReal, novoImaginaria)

    def conjugado(self):
        return Complexo(self.real, -self.imaginaria)

    def __truediv__(self, n):
        novoReal = (self.real*n.real + self.imaginaria*n.imaginaria)/(n.real**2 + n.imaginaria**2)
        novoImaginaria = (n.real*self.imaginaria - self.real*n.imaginaria)/(n.real**2 + n.imaginaria**2)
        return Complexo(novoReal, novoImaginaria)




a = Complexo(1,-1) 
b = Complexo(1,1)
c = Complexo(5,20) 



n4 = a + b * c

print(f"{n4.real} + {n4.imaginaria}i")

n5  = a/b

print(f"{n5.real} + {n5.imaginaria}i")