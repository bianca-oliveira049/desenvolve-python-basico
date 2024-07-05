import random
import math
n = int(input("Digite o valor de n: "))
soma = 0
for n in range(1, n+1, 1):
    num = random.randint(0, 100)
    print(num)
    soma += num
print(f"A raiz quadrada da soma dos {n} números aleatórios entre 0 e 100 é: ", math.sqrt(soma))