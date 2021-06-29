class Carro:
    def __init__(self, nome, marca, ano, valor) -> None:
        self.nome = nome
        self.marca = marca
        self.ano = ano
        self.valor = valor

    def acelerar(self):
        pass

    def venda(self, pagamento):
        if pagamento == self.valor:
            return 'O carro é seu, você pagou {}'.format(pagamento)
        else:
            return 'O valor {} é insuficiente!'.format(pagamento)




