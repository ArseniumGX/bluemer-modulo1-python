class Pessoa:
    def __init__(self) -> None:
        self.nome = str()
        self.idade = int()
        self.peso = float()

    def criarPessoa(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso

    def comer(self, calorias):
        if self.idade > 30:
            self.peso += calorias*2
        else:
            self.peso += calorias

    def malhar(self, calorias):
        if self.idade < 30:
            self.peso -= calorias*2
        else:
            self.peso -= calorias

    def mostrarDados(self) -> str:
        return 'Nome: {}\nIdade: {}\nPeso: {}'.format(self.nome, self.idade, self.peso)

