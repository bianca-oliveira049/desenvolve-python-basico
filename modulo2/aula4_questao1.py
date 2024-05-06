comprimento = int(input("Comprimento do terreno: "))
largura = int(input("Largura do terreno: "))
preco_m2 = float(input("Digite o preço do metro quadrado na região: "))
area_m2 = comprimento * largura
preco_total = preco_m2 * area_m2
print(f"O terreno possui {area_m2} m² e custa R${preco_total}")