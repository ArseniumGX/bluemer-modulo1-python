def decodeMorse(sequence):
    message = ''
    for i in range(len(sequence)):
        if sequence in '.- ':
            message += sequence[i]
    print(message)

decodeMorse('.... . -.--   .--- ..- -.. .')