# se a pessoa tiver mais que 30 anos as calorias de comer são em dobro
# Se a pessoa tiver menor que 30 anos as calorias de malhar são em dobro
from .classPessoa import Pessoa
from .classConta import Conta
from .classReceita import Receita

pessoa1 = Pessoa()
pessoa1.criarPessoa('José', 31, 69.5)
print(pessoa1.mostrarDados())
pessoa1.comer(4)
print(pessoa1.mostrarDados())
pessoa1.malhar(4)
print(pessoa1.mostrarDados())

pessoa2 = Pessoa()
pessoa2.criarPessoa('Anseris', 25, 55.3)
print(pessoa2.mostrarDados())
pessoa2.comer(4)
print(pessoa2.mostrarDados())
pessoa2.malhar(5)
print(pessoa2.mostrarDados())


contaX = Conta('José', 2900.00)
# print(contaX.mostrarSaldo())
contaX.sacar(1200)
# print(contaX.mostrarSaldo())
contaX.depositar(300)
# print(contaX.mostrarSaldo())
contaX.sacar(2100)
print(contaX.mostrarSaldo())

receita = Receita(3, 400, 21, 43)
receita.forno()
