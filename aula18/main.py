from conta import Conta

conta001 = Conta()
conta001.titular = 'José'
conta001.saldo = 300

print(conta001.titular)
print(conta001.saldo)

conta001.sacar(100)
print(conta001.saldo)









  















    # banco = list()

    # for i in range(2):
    #     conta = Conta(input('Titular: '))
    #     banco.appen(conta)

    # banco[0].depositar(500)
    # banco[1].depositar()
    # print(banco)