class Catalogo:
    def __init__(self) -> None:
        self.__nome = str()
        self.__ano = int()
        self.__likes = int()

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = int(ano)

    @property
    def likes(self):
        return self.__likes

    def darLike(self):
        self.__likes += 1