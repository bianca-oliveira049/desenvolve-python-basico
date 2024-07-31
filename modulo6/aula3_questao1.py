lista = []
num_elementos = int(input("Digite o número de elementos da lista: "))
for i in range(num_elementos):
    lista.append(input())
print(f"Lista: {lista[::]}")
print(f"Três primeiros elementos da lista: {lista[0:3]}")
print(f"Lista invertida: {lista[-1::-1]}")
print(f"Elementos com índice par: {lista[::2]}")
print(f"Elementos com índice ímpar: {lista[1::2]}")