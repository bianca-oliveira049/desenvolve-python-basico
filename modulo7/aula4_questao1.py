import os
frase = input("Digite uma frase: ")
arquivo = 'C:\\Users\\PDITA049\\OneDrive\\Python\\modulo7\\frase.txt'
with open (arquivo, 'w') as arq:
    arq = arq.write(frase)
print(f"Frase salva em {arquivo}")