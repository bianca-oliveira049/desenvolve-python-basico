frase = input("Digite a frase: ")
fraseModificada = ''
for caractere in frase: 
    if caractere in "aeiouAEIOU":
        caractere = '*'
    fraseModificada += caractere
print(fraseModificada)