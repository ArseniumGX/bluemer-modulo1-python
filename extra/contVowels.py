# Desafio que retorna a quantidade de vogais que uma string possui

def get_count(input_str):
    num_vowels = 0
    for i in range(len(input_str)):
        if input_str[i] in 'aeiouAEIOU':
            # print(input_str[i])
            num_vowels += 1
    
    return num_vowels

print(get_count("abracadabra"))