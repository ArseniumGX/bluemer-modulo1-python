from catalogo import Catalogo

class Filme(Catalogo):
    def __init(self) -> None:
        super().__init__()
        self.__duracao = int()

    def __str__(self):
        return 'Nome: {}\nAno: {}\nDuração: {}\nLikes: {}'.format(self.nome, self.ano, self.duracao, self.likes)
    
    @property
    def duracao(self):
        return self.__duracao

    @duracao.setter
    def duracao(self, value):
        self.__duracao = value

