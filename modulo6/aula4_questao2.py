frase = (input("Digite uma frase: "))
vogais = [letra for letra in frase if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u' or letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U']
consoantes = [letra for letra in frase if letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u' and letra != 'A' and letra != 'E' and letra != 'I' and letra != 'O' and letra != 'U' and letra != ' ']
vogais.sort()
print("Vogais:", vogais)
print("Consoantes:", consoantes)