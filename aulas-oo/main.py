from filme import Filme
from serie import Serie
from os import system


if __name__ == '__main__':
    catalogo = list()
    
    while True:

        fim = str(input('Deseja cadastrar mais títulos? [S/N]: ')).upper().strip()[0]
        while fim not in 'SN' and fim == None:
            system('clear')
            fim = str(input('Opção inválida!\nDeseja cadastrar mais títulos? [S/N]: ')).upper().strip()[0]
        if fim == 'N':
            break
        else:
            continue
