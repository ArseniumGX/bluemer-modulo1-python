from catalogo import Catalogo

class Serie(Catalogo):
    def __init(self) -> None:
        self.__temporada = int()

    def __str__(self):
        return 'Nome: {}\nAno: {}\nTemporadas: {}\nLikes: {}'.format(self.nome, self.ano, self.temporada, self.likes)
    
    @property
    def temporada(self):
        return self.__temporada

    @temporada.setter
    def temporada(self, seasson):
        self.__temporada = seasson