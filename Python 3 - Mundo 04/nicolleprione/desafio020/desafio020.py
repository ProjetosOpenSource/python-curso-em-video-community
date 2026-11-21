from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.jogador = nome
        self.usuario = nick
        self.jogos_fav = []

    def add_jogos(self, jogo):
        self.jogos_fav.append(jogo)
    
    def dados(self):
        texto = f'[white]Nome:[/] {self.jogador} \n[white]Nick:[/] {self.usuario} \n[white]Jogos Favoritos:[/]'
        for jogos in self.jogos_fav:
            texto += f'\n\t* {jogos}'
        painel = Panel(texto, title='DADOS DO JOGADOR', style='bold purple', width=35)
        return painel


jog01 = Gamer('Pedro', 'TicoTico')
jog01.add_jogos('GTV 6')
jog01.add_jogos('Fifa 27')
print(jog01.dados())