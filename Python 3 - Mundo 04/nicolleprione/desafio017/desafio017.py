class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        return f'Produto = {self.nome} | R$ {self.preco:,.2f}'

produto01 = Produto('Notebook', 3500)
print(produto01.etiqueta())

produto02 = Produto('Mouse', 124.90)
print(produto02.etiqueta())