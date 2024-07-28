lista1 = []
lista2 = []
lista3 = []
indice = 0
tamLista1 = int(input("Digite a quantidade de elementos da lista 1: "))
print("Digite os elementos da lista 1:")
for i in range(tamLista1):
    lista1.append(int(input()))
tamLista2 = int(input("Digite a quantidade de elementos da lista 2: "))
print("Digite os elementos da lista 2:")
for i in range(tamLista2):
    lista2.append(int(input()))
if len(lista1) <= len(lista2):
    while lista1[-1] not in lista3:
        lista3.append(lista1[indice])
        lista3.append(lista2[indice])
        indice += 1
    for indice in range(indice, tamLista2, 1):
        lista3.append(lista2[indice])
else:
    while lista2[-1] not in lista3:
        lista3.append(lista1[indice])
        lista3.append(lista2[indice])
        indice += 1
    for indice in range(indice, tamLista1, 1):
        lista3.append(lista1[indice])
print(f"Lista intercalada: {lista3}")
