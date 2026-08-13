class Gamer:
    """
    Representa um jogador e sua lista de jogos favoritos.

    Attributes:
        nome (str): Nome real do jogador.
        nick_name (str): Apelido/Nick do jogador nos jogos.
        jogos_fav (list[str]): Lista com os nomes dos jogos favoritos.
    """
    def __init__(self, nome, nick_name):
        self.nome = nome
        self.nick_name = nick_name
        self.jogos_fav = []

    def add_jogos(self, jogo):
        self.jogos_fav.append(jogo)

    def ficha(self):
        print('=' * 10)
        texto = f"""Nome: {self.nome}
Jogador(a): {self.nick_name}
Jogos Favoritos:"""
        for jogo in self.jogos_fav:
            texto += f'\n* {jogo}'
        print(texto)
        print('=' * 10)