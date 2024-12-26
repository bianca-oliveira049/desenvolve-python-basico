frase = input("Digite a frase: ")
espacos = 0
for caractere in frase:
    if caractere == ' ': espacos += 1
print(f"Espaços em branco: {espacos}")