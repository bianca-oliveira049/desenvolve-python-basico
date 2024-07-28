from random import randint
elementos = []
num_elementos = randint(5, 20)
for i in range(num_elementos):
    elementos.append(randint(1, 10))
print("Lista de elementos:", elementos)
print("Soma dos elementos da lista:", sum(elementos))
print("Média dos elementos da lista:", sum(elementos) / len(elementos))