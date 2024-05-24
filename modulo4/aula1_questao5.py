n = int(input("Digite o número de idades: "))
soma_idades = 0
cont = 0
while cont < n:
    idade = int(input("Digite a idade: "))
    soma_idades += idade
    cont += 1
print(soma_idades / n)