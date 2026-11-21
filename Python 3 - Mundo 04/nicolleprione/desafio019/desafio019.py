from rich import print
from rich.panel import Panel

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.qtd_pag = paginas
        self.pag_atual = 1

    def passagem_pagina(self, valor = 1):
        for pag in range(valor):
            if not self.fim_livro():
                self.pag_atual += 1
                print(f'Pág {self.pag_atual} -> ', end='')
        print(f'Página atual: {self.pag_atual}')
        
    def fim_livro(self):
        if self.pag_atual == self.qtd_pag:
            return True
        else:
            return False

    def dados(self):
        texto = (f'[bold][blue]Titulo:[/] [green]{self.titulo}[/] | [blue]Páginas:[/] [green]{self.qtd_pag}[/] | [blue]Página atual:[/] [green]{self.pag_atual}[/][/]')
        painel = Panel(texto, title='[bold red]LIVRO ATUAL[/]', width=60)
        return painel

livro01 = Livro('Metamorfose', 20)
print(livro01.dados())
livro01.passagem_pagina(5)
livro01.passagem_pagina(10)
livro01.passagem_pagina(30)