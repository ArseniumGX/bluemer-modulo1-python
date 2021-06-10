""" 
Calculadora de Dano - Escreva um programa que receba dois valores digitados pelo usuário:

    Quantidade de vida de um monstro (entre 10 e 50);
    Valor do ataque do jogador por turno (entre 5 e 10);
    Baseado nos valores digitados, exiba a quantidade de turnos que o jogador irá demorar para conseguir derrotar o monstro.

    O jogador irá derrotar o monstro em 8 turnos.
"""
from math import ceil


hp = int(input("Quantidade de vida de um monstro (entre 10 e 50): "))
hit = int(input("Valor do ataque do jogador por turno (entre 5 e 10): "))

turnos = ceil(hp/hit)

print(f'\nO jogador irá derrotar o monstro em {turnos} turnos.')