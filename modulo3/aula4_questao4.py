distancia = float(input("Digite a distância de entrega em km: "))
peso = float(input("Digite o peso do pacote em kg: "))
if (distancia <= 100):
    frete = 1 * peso
if (distancia >= 101 and distancia <= 300):
    frete = 1.5 * peso
if (distancia > 300):
    frete = 2 * peso
if (peso > 10):
    frete = frete + 10
print(f"Frete: R${frete:.2f}")