from random import randint
valores = []
for n in range(20):
    valores.append(randint(-100, 100))
print("Lista de valores ordenada:", sorted(valores))
print("Lista de valores:", valores)
print("Índice do maior valor da lista:", valores.index(max(valores)))
print("Índice do menor valor da lista:", valores.index(min(valores)))