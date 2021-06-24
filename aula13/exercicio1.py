# Faça um programa que tenha uma função chamada voto() que 
# vai receber como parâmetro o ano de nascimento de uma 
# pessoa, retornando um valor literal indicando se uma pessoa
# tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições: 


def voto(ano:int):
    from datetime import date

    idade = date.today().year - ano
    if 16 <= idade < 18 or idade >= 70:
        return 'Voto Opcional'
    elif idade in range(18, 70):
        return 'Voto Obrigatório'
    else:
        return 'Voto Negado'

print(voto(1990)) # 31, expected Voto Obrigatório
print(voto(2008)) # 13, expected Voto Negado
print(voto(1951)) # 70, expected Voto Opcional
print(voto(2005)) # 16, expected Voto Opcional
print(voto(2003)) # 18, expectev Voto Obrigatório
print(voto(1952)) # 69, expected Voto Obrigatório
