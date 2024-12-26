celular = input("Digite o número: ")
if len(celular) == 8: celular = '9' + celular
if celular[0] == '9': celular = celular[0:5] + '-' + celular[5:]
print(f"Número completo: {celular}")