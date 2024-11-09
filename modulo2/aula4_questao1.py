#entrada do comprimento do terreno
comprimento = int(input("Comprimento do terreno: "))
#entrada da largura do terreno
largura = int(input("Largura do terreno: "))
#entrada do preço do metro quadrado
preco_m2 = float(input("Digite o preço do metro quadrado na região: "))
#cálculo da área do terreno
area_m2 = comprimento * largura
#cálculo do preço do terreno levando em consideração a área calculada e o preço fornecido pelo usuário
preco_total = preco_m2 * area_m2
#impressão do resultado
print(f"O terreno possui {area_m2} m² e custa R${preco_total}")
