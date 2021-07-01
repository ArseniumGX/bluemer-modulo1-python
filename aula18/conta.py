class Conta:
    def __init__(self, titular, saldo = 0):
        self.titular = titular
        self.__saldo = saldo

    def __str__(self):
        if self.__saldo == 0:
            return f'''
            Titular: {self.titular}
            '''
        else:
            return f'''
            Titutar: {self.titular}
            Saldo : {self.__saldo}
            '''

    def depositar(self, valor):
        self.__saldo += valor
        return f'''
        {self.titular} seu saldo atual é de {self.__saldo}
        '''

    def sacar(self, valor):
        if self.__saldo > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            return f'''
            {self.titular} seu saldo atual é de {self.__saldo}
            '''
        else:
            return 'Saldo insuficiente.'
