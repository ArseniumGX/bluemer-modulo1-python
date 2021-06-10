""" 
Crie um programa em Python que peça a nota do aluno, que deve ser um float entre 0.00 e 10.0

    Se a nota for menor que 6.0, deve exibir a nota F.

    Se a nota for de 6.0 até 7.0, deve exibir a nota D.

    Se a nota for entre 7.0 e 8.0, deve exibir a nota C.

    Se a nota for entre 8.0 e 9.0, deve exibir a nota B.

    Por fim, se for entre 9.0 e 10.0, deve exibir um belo de um A
"""

valor = float(input("Digite uma nota entre 0.0~10.0: "))

if valor >= 0.0 and valor <= 10.0:
    if valor < 6.0:
        print("Nota F.")
    elif valor >= 6.0 and valor < 7.0:
        print("Nota D.")
    elif valor >= 7.0 and valor < 8.0:
        print("Nota C.")
    elif valor >= 8.0 and valor < 9.0:
        print("Nota B.")
    else:
        print("Nota A.")
else:
    print("Nota inválida!")