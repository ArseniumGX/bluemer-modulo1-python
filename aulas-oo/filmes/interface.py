from os import system

while True:
    print('''
    +------=== Catágolo de Filmes ===------+

        [ 1 ] Cadastrar
        [ 2 ] Alterar
        [ 3 ] Excluir
        [ 4 ] Mostrar
        [ 0 ] Voltar
    ''')

    

    opcao = input('\t\t\t  [ ')
    while not opcao.isnumeric():
        opcao = input('\t\t\t  [ ')
    opcao = int(opcao)

    if opcao in [1,2,3,4]:
        pass
