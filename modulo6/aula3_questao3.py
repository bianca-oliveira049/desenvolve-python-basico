from random import randint
inicioAtual = 0
tamIntervaloAtual = 0
inicio = 0
tamIntervalo = 0
elementos = []
for i in range(20):
    elementos.append(randint(-10, 10))
print(f"Original: {elementos}")
for i in range(20):
    if elementos[i] < 0:
        tamIntervaloAtual += 1
        if tamIntervaloAtual == 1:
            inicioAtual = i
    else:
        if tamIntervaloAtual > tamIntervalo:
            tamIntervalo = tamIntervaloAtual
            inicio = inicioAtual
        tamIntervaloAtual = 0

del elementos[inicio:inicio + tamIntervalo:1]
print(f"Editada: {elementos}")


                
            