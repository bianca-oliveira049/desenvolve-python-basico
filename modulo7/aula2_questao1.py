nascimento = input("Digite a data de nascimento (dd/mm/aaa): ")
data = nascimento.split("/")
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
print(f"Você nasceu em {data[0]} de {meses[int(data[1]) - 1]} de {data[2]}")