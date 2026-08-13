import churrasco

def main():
    casamento = churrasco.Churrasco(50, 'Casamento')
    casamento.resumo()

    aniversario = churrasco.Churrasco(20, 'Aniversario')
    aniversario.resumo()

if __name__ == '__main__':
    main()