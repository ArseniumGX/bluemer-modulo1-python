from filme import Filme
from serie import Serie
from os import system


if __name__ == '__main__':
    catalogo = list()
    
    while True:
        system('clear')

        print('''
        +------=== Locadora Bugada ===------+
           
            [ 1 ] Filmes
            [ 2 ] Séries
        
            [ 0 ] Encerrar
        ''')

        locadora = input('\t    [ ')
        while not locadora.isnumeric():
            locadora = input('\t|\tOpção Inválida!\n\t    [ ')
        locadora = int(locadora)

        if locadora == 1:
            pass
        elif locadora == 2:
            pass
        elif locadora == 0:
            system('clear')
            break
        else:
            continue
