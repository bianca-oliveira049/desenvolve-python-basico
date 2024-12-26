frase = input("Digite uma frase: ")
indices = []
vogais = 0
for i in range(len(frase)):
    if frase[i] in 'aeiou': 
        vogais += 1
        indices.append(i)
print(f"{vogais} vogais")
print(f"Índices: {indices}")