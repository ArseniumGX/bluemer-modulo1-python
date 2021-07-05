# Projeto 04 - Voto Votado

from datetime import date
from random import choice
from time import sleep

## Função pra limpar terminal
def clear():
    import platform
    import os
    if platform.system() == 'Windowns':
        os.system('cls')
    elif platform.system() == 'Linux':
        os.system('clear')
    else:
        return None

def autorizaVoto(anoNascimento:int):
    idade = date.today().year - anoNascimento
    if 0 < idade < 16:
        return('NEGADO')
    elif idade in range(16, 18) or idade >= 70:
        return('OPCIONAL')
    else:
        return('OBRIGATÓRIO')

def votacao(auth, voto):
    if auth == 'NEGADO':
        return "\n\n\t\tVocê não pode votar."
        
    elif auth == 'OPCIONAL' or auth == 'OBRIGATÓRIO' and voto == 1:
        urna[0]['votos'] += 1
        return '\n\n\t\tVoto computado.'
    elif auth == 'OPCIONAL' or auth == 'OBRIGATÓRIO' and voto == 2:
        urna[1]['votos'] += 1
        return '\n\n\t\tVoto computado.'
    elif auth == 'OPCIONAL' or auth == 'OBRIGATÓRIO' and voto == 3:
        urna[2]['votos'] += 1
        return '\n\n\t\tVoto computado.'
    elif auth == 'OPCIONAL' or auth == 'OBRIGATÓRIO' and voto == 4:
        urna[3]['votosNulos'] += 1
        return '\n\n\t\tVoto computado.'
    elif auth == 'OPCIONAL' or auth == 'OBRIGATÓRIO' and voto == 5:
        urna[4]['votosBrancos'] += 1
        return '\n\n\t\tVoto computado.'
    else:
        # else desnecessário, so coloquei pois me incomoda tantos if..elif aninhados sem um else no fim
        #
        return None

# Escolha para os candidatos aleatorios na lista
candidatoA = choice(['Pure', 'Material UI', 'Semantic UI', 'Materialize', 'Bootstrap'])
candidatoB = choice(['Django', 'ExpressJS', 'Flask', 'Koa', 'Spring Boot'])
candidatoC = choice(['NodeJS', 'Java', 'Python', 'PHP', 'Typescript'])

# inicialzação de uma list de dict onde vai armazenar todos os votos
urna = [{'candidato': candidatoA, 'votos': int()},
        {'candidato': candidatoB, 'votos': int()},
        {'candidato': candidatoC, 'votos': int()},
        {'votosNulos': int()},
        {'votosBrancos': int()}]


while True:
    clear()

    # Valida que o que o usuário dititar é numérico
    auth = input('Digite seu ano de seu nascimento: ')
    while not auth.isnumeric():
        print('Apenas números!')
        auth = input('Digite seu ano de seu nascimento: ')
    auth = int(auth)
    
    clear()
    
    print('''
    +---------======-{{ VOTAÇÃO }}-======---------
    |
    |   [ 1 ] - {}
    |   [ 2 ] - {}
    |   [ 3 ] - {}
    |
    |   [ 4 ] - VOTO NULO
    |   [ 5 ] - VOTO EM BRANCO
    |
    |   [ 0 ] - FINALIZAR PROGRAMA
    |'''.format(candidatoA, candidatoB, candidatoC))

    # mesma validação que no ano, preferi fazer como um menu ja convertendo 
    # em int pra evitar possiveis erros nas conficionais na função acima
    options = input('    +---[ ').strip()
    while not options.isnumeric():
        print('\t\tInválido!')
        options = input('    +---[ ').strip()
    options = int(options)

    # para todas as opção da lista
    if options in [1, 2, 3, 4, 5]:
        print(votacao(autorizaVoto(auth), options))
        sleep(2)

    # Opção término da eleição em caso de opção == 0
    elif options == 0:
        clear()
        break

    # Condicional força o loop para a próxima interação caso options seja diferente de 0 1 2 3 4 5
    # Nesse caso vai ser preciso entar novamente com o ano de nascimento
    else:
        print('\t\tOpção inválida!')
        input('\t  Tecle Enter para continuar...')
        continue


# variável que apenas contabiliza o total de votos dentro do laço a seguir já passando a
# soma de votos nulos e brancos
totalVotos = urna[3]['votosNulos'] + urna[4]['votosBrancos']
for i in range(3):
    totalVotos += urna[i]['votos']
    print('\tCandidato {} recebeu {} votos'.format(urna[i]['candidato'], urna[i]['votos']))

print('''
\t\tVotos Nulos: {}\n\t\tVotos em Branco: {}\n\n\t\tTota de Votos: {}
    '''.format(urna[3]['votosNulos'], urna[4]['votosBrancos'], totalVotos))


votosValidos = 0 # variável que contabiliza apenas os votos válidos em cada candidato
temp = 0 # variável temporária para armazenar o maior número de votos que um candidato teve para comparação no if no laço abaixo
vencedor = None # variável quem que vai receber uma copia do dict com as informações do candidato mais votado
for i in range(3):
    votosValidos += urna[i]['votos']
    if urna[i]['votos'] > temp:
        temp = urna[i]['votos']
        vencedor = urna[i].copy()


print(f"O candidato {vencedor['candidato']} venceu a eleição com {round(100 * vencedor['votos']/votosValidos, 2)}% dos votos válidos.")
input('\t\tTecle enter para continuar...')
clear()
