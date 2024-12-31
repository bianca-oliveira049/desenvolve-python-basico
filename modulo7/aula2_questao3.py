while True:
    frase = input('Digite uma frase (digite "fim" para encerrar):' )
    fraseUnida = ''
    if frase == 'fim': break
    for caractere in frase:
        if not(ord(caractere) >= 33 and ord(caractere) <= 47 or ord(caractere) >= 58 and ord(caractere) <= 63 or caractere == ' '): 
            fraseUnida += caractere
    i = 0        
    j = -1
    fraseUnida = fraseUnida.lower()
    palindromo = False
    while j > -len(fraseUnida) and i < len(fraseUnida):
        if fraseUnida[i] == fraseUnida[j]: palindromo = True
        else: palindromo = False
        i += 1
        j -= 1
    if palindromo: print(f'"{frase}" é palíndromo')
    else: print(f'"{frase}" não é palíndromo')
        