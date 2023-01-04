
class Pessoa(Observador):
    
    def __init__(self):
        self.acordada = False

    def esta_acordada(self):
        return self.acordada

    def atualizar(self):
        print("acordei")
        self.acordada = True