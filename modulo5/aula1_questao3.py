import random
num = random.randint(1, 10)
while True:
    resp = int(input("Adivinhe o número entre 1 e 10: "))
    if resp != num:
        if resp > num:
            print("Muito alto, tente novamente!")
        elif resp < num:
            print("Muito baixo, tente novamente!")
    else:
        print(f"Correto! O número é {num}")
        break