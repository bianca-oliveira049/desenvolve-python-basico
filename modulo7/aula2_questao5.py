import random
def embaralhar_palavras(frase):
    palavras = frase.split()
    fraseEmbaralhada = ''
    for palavra in palavras:
        palavraEmbaralhada = ''
        if len(palavra) > 1:
            meioPalavra = ''
            for i in range(1, len(palavra)-1):
                meioPalavra += palavra[i]
            meioEmbaralhada = ''.join(random.sample(meioPalavra, len(meioPalavra)))
            palavraEmbaralhada = palavra[0] + meioEmbaralhada + palavra[-1]
        else: palavraEmbaralhada = palavra
        fraseEmbaralhada += ' ' + (palavraEmbaralhada)
        print(fraseEmbaralhada)
    return fraseEmbaralhada
frase = input("Digite a frase: ")
resultado = embaralhar_palavras(frase)
print(resultado)
