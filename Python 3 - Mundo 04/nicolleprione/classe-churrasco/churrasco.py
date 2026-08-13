class Churrasco:
    """
    Calcula e gerencia o consumo de carne e os custos de um churrasco.

    Attributes:
        consumo_padrao (float): Consumo estimado de carne por pessoa em KG (Padrão: 0.400 KG).
        valor_padrao (float): Preço médio por quilo de carne em Reais (Padrão: R$ 82.40).
        pessoas (int): Quantidade total de participantes do churrasco.
        churras (str): Nome ou evento do churrasco (ex: "Aniversário", "Casamento").
    """
    consumo_padrao = 0.400
    valor_padrao = 82.40

    def __init__(self, qtd_pessoas, nome_churrasco):
        self.pessoas = qtd_pessoas
        self.churras = nome_churrasco

    def total_carne(self):
        carne = self.pessoas * Churrasco.consumo_padrao
        return carne

    def total_valor(self):
        valor = self.total_carne() * Churrasco.valor_padrao
        return valor

    def total_pessoa(self):
        valor_pessoa = self.total_valor() / self.pessoas
        return valor_pessoa

    def resumo(self):
        print('-' * 40)
        texto = f"""Churrasco para: {self.churras}
* Quantidade de pessoas: {self.pessoas}
* Quantidade de carne: {self.total_carne():.3f} KG
* Valor total: R$ {self.total_valor():,.2f}
* Valor por pessoa: R$ {self.total_pessoa():.2f}"""
        print(texto)
        print('-' * 40)