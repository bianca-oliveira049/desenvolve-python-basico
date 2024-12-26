frase = input("Digite a frase: ")
palavraObj = input("Digite a palavra objetivo: ")
anagramas = []
i = 0
anagrama = False
palavras = frase.split()
for conjunto in palavras:
    if len(palavraObj) == len(conjunto):
        for letra in conjunto:
            if conjunto.count(letra) == palavraObj.count(letra):
                anagrama = True
            else: anagrama = False
    else: anagrama = False
    if anagrama: anagramas.append(conjunto)        
print(f"Anagramas: {anagramas}")



