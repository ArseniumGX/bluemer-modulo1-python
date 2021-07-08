# Retorna a proximo numero que possuo uma raiz quadrada perfeita se o paramtro passado
# safisfaz a mesma condição, caso contrario retorna -1

def find_next_square(sq):
    if int(sq ** 0.5) * int(sq ** 0.5) == sq:
        while True:
            sq += 1
            if int(sq ** 0.5) * int(sq ** 0.5) == sq:
                return sq
    else:
        return -1


print(find_next_square(121))
print(find_next_square(155))
print(find_next_square(0))


