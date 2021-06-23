# 2. Exercício  Treino - 
# Crie  um  dicionário  em  que  suas  chaves  correspondem  
# a  números inteiros entre [1, 10] e cada valor associado é 
# o número ao quadrado. 
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

dicio = dict() or {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: None}

for i in dicio:
    dicio[i] = i ** 2

print(dicio)