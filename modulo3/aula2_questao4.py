classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ")
pontosForca = int(input("Digite os pontos de força (de 1 a 20): "))
pontosMagia = int(input("Digite os pontos de magia (de 1 a 20): "))
validarFicha = (classe == "guerreiro" and pontosForca >= 15 and pontosMagia <=10) or (classe == "mago" and pontosForca <= 10 and pontosMagia >= 15) or (classe == "arqueiro" and (pontosForca > 5 and pontosForca <= 15) and (pontosMagia > 5 and pontosMagia <= 15))
print(f"Pontos de atributo consistentes com a classe escolhida: {validarFicha}")