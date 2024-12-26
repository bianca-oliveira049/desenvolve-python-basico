cpf = input("Digite o CPF: ")
somaDigito1 = 0
somaDigito2 = 0
multiplicador = 10
for i in range(11):
    if cpf[i] == '.': continue
    somaDigito1 += int(cpf[i]) * multiplicador
    multiplicador -= 1
if somaDigito1 % 11 < 2: digito1 = 0
else: digito1 = 11 - (somaDigito1 % 11)
multiplicador = 11
for i in range(13):
    if cpf[i] == '.' or cpf[i] == '-': continue
    somaDigito2 += int(cpf[i]) * multiplicador
    multiplicador -= 1
if somaDigito2 % 11 < 2: digito2 = 0
else: digito2 = 11 - (somaDigito2 % 11)  
if int(cpf[12]) == digito1 and int(cpf[13]) == digito2: print("CPF válido")
else: print("CPF inválido")
