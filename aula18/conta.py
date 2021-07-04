class Conta:
    def __init__(self):
        self.__titular = str()
        self.__saldo = float()

    def __str__(self):
        if self.__saldo == 0:
            return f'''
            Titular: {self.__titular}
            '''
        else:
            return f'''
            Titutar: {self.__titular}
            Saldo : {self.__saldo}
            '''

    def depositar(self, valor):
        self.__saldo += valor
        return f'''
        {self.__titular} seu saldo atual é de {self.__saldo}
        '''

    def __autorizaSaque(self, valor):
        return self.__saldo > 0 and valor <= self.__saldo

    def sacar(self, valor):
        if self.__autorizaSaque(valor):
            self.__saldo -= valor
            return f'''
            {self.__titular} seu saldo atual é de {self.__saldo}
            '''
        else:
            return 'Saldo insuficiente.'

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor
    
    
    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, name):
        self.__titular = name