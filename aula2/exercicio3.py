""" 
03 - Você está na flor da idade?

    Defina uma variável para o valor do ano do nascimento;
    Defina uma variável para o valor do ano atual;
    Defina uma variável que calcula o valor final da idade da pessoa;
    Exiba uma mensagem final dizendo a idade da pessoa e a mensagem "Você está na flor da idade".

"""

ano_nasc = int(input("Digite o ano do seu nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade = ano_atual - ano_nasc

print(f'Você tem {idade}\nVocẽ está na flor da idade.')
