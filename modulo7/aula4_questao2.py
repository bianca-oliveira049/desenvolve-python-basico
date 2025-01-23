with open ('C:\\Users\\PDITA049\\OneDrive\\Python\\modulo7\\frase.txt', 'r') as frase:
    apenasPalavras = []
    linha = frase.readline()
    linha = linha.split(' ')
    for palavra in linha:
        palavraSemPontuacao = ''
        for caractere in palavra:
            if ord(caractere) >= 65 and ord(caractere) <= 90 or ord(caractere) >= 97 and ord(caractere) <= 122: 
                palavraSemPontuacao += caractere
        apenasPalavras.append(palavraSemPontuacao + '\n')
        print(apenasPalavras)
with open ('palavras.txt', 'w') as palavras:
    palavras.writelines(apenasPalavras)
with open ('palavras.txt', 'r') as palavras:
    print(palavras.read())


        
