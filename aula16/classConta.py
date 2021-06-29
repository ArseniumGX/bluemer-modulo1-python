# Crie uma classe chamada Conta para simular as operações 
# de uma conta corrente. Sua classe deverá ter os atributos 
# Titular e Saldo, e os métodos Sacar e Depositar. Crie um 
# objeto da classe Conta e teste os atributos e métodos 
# implementados.​ Adicione uma regra no método Sacar, onde o 
# usuário só poderá sacar se o Saldo for maior que zero, caso 
# contrário mostre a mensagem na tela: 
# "Você não tem saldo suficiente para essa operação." 

class Conta:
    def __init__(self, titular, saldo) -> None:
        self.titular = titular
        self.saldo = saldo

    def sacar(self, value):
        if self.saldo > 0 and value <= self.saldo:
            self.saldo -= value
        else:
            self.error()

    def depositar(self, value):
        if value > 0:
            self.saldo += value
        else:
            self.error()

    def mostrarSaldo(self):
        return 'Titular: {}\nSaldo: {}'.format(self.titular, self.saldo)

    def error(self) -> str:
        print('Operação inválida ou recusada.')
