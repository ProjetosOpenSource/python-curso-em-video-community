class Funcionario:

    empresa = 'Jupiter'

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f'Olá, meu nome {self.nome}, sou {self.cargo} no setor de {self.setor} da empresa {Funcionario.empresa}'

func01 = Funcionario('João', 'RH', 'Analista')
print(func01.apresentacao())

func02 = Funcionario('Patricia', 'Financeiro', 'Auxiliar Contabil')
print(func02.apresentacao())