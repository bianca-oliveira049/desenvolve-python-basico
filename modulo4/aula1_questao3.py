n1 = int(input("Digite o valor de n1: "))
n2 = int(input("Digite o valor de n2: "))
n3 = int(input("Digite o valor de n3: "))
while n1 >= 0 and n2 >= 0 and n3 >= 0:
    m = (n1 + n2 + n3) / 3
    if m >= 60:
        print("Aprovado")
    elif m >= 40:
        print("Recuperação")
    else:
        print("Reprovado")
    n1 = int(input("Digite o valor de n1: "))
    n2 = int(input("Digite o valor de n2: "))
    n3 = int(input("Digite o valor de n3: "))
print("Fim")