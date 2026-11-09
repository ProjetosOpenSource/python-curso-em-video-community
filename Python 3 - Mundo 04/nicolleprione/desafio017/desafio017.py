from rich import print
from rich.table import Table

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        tabela = Table(title='Tabela de Preços')

        tabela.add_column('PRODUTO', justify='center', style='blue')
        tabela.add_column('PREÇO', justify='center', style='green')

        tabela.add_row(self.nome, f'R$  {self.preco:,.2f}')

        return tabela

produto01 = Produto('Notebook', 3500)
print(produto01.etiqueta())

produto02 = Produto('Mouse', 122.99)
print(produto02.etiqueta())

produto03 = Produto('Teclado', 210)
print(produto03.etiqueta())