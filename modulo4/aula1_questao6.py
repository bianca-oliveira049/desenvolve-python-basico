N = int(input("Digite o número de experimentos realizados: "))
cont = 0
total_cobaias = 0
total_c = 0
total_s = 0
total_r = 0
while cont < N:
    quantia = int(input("Digite a quantidade de cobaias: "))
    tipo_cobaia = (input("Digite o tipo de cobaia (S/C/R): "))
    total_cobaias += quantia
    if tipo_cobaia == 'C':
        total_c += quantia
    elif tipo_cobaia == 'S':
        total_s += quantia
    elif tipo_cobaia == 'R':
        total_r += quantia
    cont += 1
percent_c = (total_c / total_cobaias) * 100
perecent_r = (total_r / total_cobaias) * 100
percent_s = (total_s / total_cobaias) * 100
print(f"Total: {total_cobaias} cobaias")
print(f"Total de coelhos: {total_c}")
print(f"Total de ratos: {total_r}")
print(f"Total de sapos: {total_s}")
print(f"Percentual de coelhos: {percent_c:.2f}%")
print(f"Percentual de ratos: {perecent_r:.2f}%")
print(f"Percentual de sapos: {percent_s:.2f}%")