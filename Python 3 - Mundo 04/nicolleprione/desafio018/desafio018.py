from rich import print
from rich.panel import Panel

class Churrasco:
    consumo_padrao:float = 0.400
    valor_padrao:float = 82.40

    def __init__(self, qtd_pessoas, titulo):
        self.qtd_pessoas = qtd_pessoas
        self.titulo = titulo
    
    def calculo_consumo(self):
        return self.qtd_pessoas * Churrasco.consumo_padrao

    def calculo_valor(self):
        return self.calculo_consumo() * Churrasco.valor_padrao

    def calculo_valor_pessoa(self):
        return self.calculo_valor() / self.qtd_pessoas

    def resumo(self):
        texto = f'Quantidade de pessoas: [bold white]{self.qtd_pessoas}[/] \nValor total: [bold white]R$ {self.calculo_valor():,.2f}[/] \nTotal de Carne: [bold white]{self.calculo_consumo():.3f}Kg[/] \nValor por Pessoa: [bold white]R$ {self.calculo_valor_pessoa():.2f}[/]'
        dados = Panel(texto, title=f'[bold blue]{self.titulo}[/]', style="bold green", width=40)
        return dados

churras01 = Churrasco(15, 'Aniversario')
print(churras01.resumo())

churras02 = Churrasco(50, 'Casamento')
print(churras02.resumo())

churras03 = Churrasco(84, 'Confraternização')
print(churras03.resumo())