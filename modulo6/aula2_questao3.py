from random import randint
lista1 = []
lista2 = []
interseccao = []
for i in range(20):
    lista1.append(randint(0, 50))
    lista2.append(randint(0, 50))
print(lista1)
print(lista2)
for elemento in lista1:
    if elemento in lista2 and elemento not in interseccao:
            interseccao.append(elemento)
interseccao.sort()
print(interseccao)
print("Contagem")
for n in interseccao:
    print(f"{n}: (lista1 = {lista1.count(n)}, lista2 = {lista2.count(n)})")

