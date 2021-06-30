# Crie uma classe que modele uma pessoa:
# 
# a) Atributos: nome, idade, peso e altura.
# b) Métodos: envelhecer, engordar, emagrecer, crescer.
# 
# Por padrão, a cada ano que a pessoa envelhece, sendo a idade
# dela menor que 21 anos, ela deve crescer 0,5 cm

from time import sleep
from os import system

class Pessoa:
    def __init__(self):
        self.nome = str()
        self.idade = int()
        self.peso = float()
        self.altura = int()

    def novaPessoa(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        if self.idade < 21:
            self.altura = self.altura + 0.5 # 1.73m + 0.005 == 173 cm + 0.5 cm
        self.idade += 1

    def engordar(self, calorias):
        self.peso += calorias

    def emagrecer(self, calorias):
        self.peso -= calorias

    def crescer(self, altura):
        self.altura += altura

    def info(self):
        return 'Nome: {}\nIdade: {}\nPeso: {}\nAltura: {}'.format(self.nome, self.idade, self.peso, self.altura)


while True:
    system('clear')
    print('''-----===----{ LIFE SIMULATOR }----===-----
    [ 1 ] Cria nova pessoa
    [ 2 ] Mostra pessoa
    [ 3 ] Engordar
    [ 4 ] Emagrecer
    [ 5 ] Envelhecer 1 ano

    [ 0 ] ENCERRAR PROGRAMA
    ''')

    opcao = input('____: ')
    while not opcao.isnumeric():
        opcao = input('____: ')
    opcao = int(opcao)

    if opcao == 1:
        system('clear')
        pessoa = Pessoa()
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        peso = float(input('Peso: '))
        altura = float(input('Altura: '))
        pessoa.novaPessoa(nome, idade, peso, altura)

    elif opcao == 2:
        system('clear')
        print(pessoa.info())
        sleep(5)

    elif opcao == 3:
        system('clear')
        cal = int(input('Número de calorias: '))
        pessoa.engordar(cal)

    elif opcao == 4:
        system('clear')
        cal = int(input('Número de calorias: '))
        pessoa.emagrecer(cal)

    elif opcao == 5:
        pessoa.envelhecer()

    elif opcao == 0:
        system('clear')
        break
    else:
        system('clear')
        continue

