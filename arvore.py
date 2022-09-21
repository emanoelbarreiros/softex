class No:
    def __init__(self, valor, esq, dir):
        self.valor = valor
        self.esq = esq
        self.dir = dir

class Arvore:
    def __init__(self, valor):
        self.raiz = No(valor, None, None)

    def inserir(self, valor):
        if valor > self.raiz.valor:
            filhoDireito = self.raiz.dir
            filhoDireito.valor



arv = Arvore(25)