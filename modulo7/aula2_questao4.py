def validador_senha(senha):
    tamanho = False
    maiuscula = False
    minuscula = False
    numero = False
    especial = False
    if len(senha) >= 8: tamanho = True
    for caractere in senha:
        if ord(caractere) >= 65 and  ord(caractere) <= 90: 
            maiuscula = True
            continue
        elif ord(caractere) >= 97 and  ord(caractere) <= 122:
            minuscula = True
            continue
        elif ord(caractere) >= 33 and  ord(caractere) <= 47 or ord(caractere) >= 58 and  ord(caractere) <= 64 or ord(caractere) >= 91 and  ord(caractere) <= 96 or ord(caractere) >= 123 and  ord(caractere) <= 127:
            especial = True
            continue
        elif ord(caractere) >= 48 and  ord(caractere) <= 57:
            numero = True
        continue
    return tamanho and maiuscula and minuscula and numero and especial