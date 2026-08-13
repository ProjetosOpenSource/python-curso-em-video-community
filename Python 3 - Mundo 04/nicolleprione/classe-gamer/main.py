import gamer

def main():
    pedro = gamer.Gamer('Pedro', 'Guerreiro98')
    pedro.add_jogos('Mortal Kombat')
    pedro.add_jogos('Fifa 26')
    pedro.add_jogos('Resident Evil')
    pedro.ficha()

    maria = gamer.Gamer('Maria', 'FeiticeiraScarlat')
    maria.add_jogos('Zelda')
    maria.add_jogos('Tomb Raider')
    maria.add_jogos('Final Fantasy V')
    maria.ficha()

if __name__ == '__main__':
    main()