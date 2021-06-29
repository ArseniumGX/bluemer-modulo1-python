from time import sleep

class Receita:
    def __init__(self, ovo, leite, farinha, manteiga) -> None:
        self.ovo = ovo
        self.leite = leite
        self.farinha = farinha
        self.manteiga = manteiga

    def misturar(self):
        if self.ovo == 2:
            return 'Bolo sendo misturado'
        else:
            return 'Você precisa de 2 ovo para misturar o bolo'

    def forno(self):
        print('Bolo sendo preparado...')
        sleep(2)
        print('Seu bolo está pronto!')

