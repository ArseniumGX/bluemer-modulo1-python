# desafio que consiste em ler um frase passada e reverte todas as palavra que tiver
# tamanho igual ou maior que 5, e retornar a frase montada

def spinWords(s):
    nova = ''
    for i in range(len(s.split())):
        if len(s.split()[i]) >= 5:
            nova += s.split()[i][::-1] + ' '
        else:
            nova += s.split()[i] + ' '
    return nova.strip()

print(spinWords("This is another test"))