from .conta import Conta


if __name__ == "__main__":
    banco = list()

    for i in range(2):
        conta = Conta(input('Titular: '))
        banco.appen(conta)

    banco[0].depositar(500)
    banco[1].depositar()
    print(banco)