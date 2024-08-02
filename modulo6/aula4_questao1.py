nums = [1,2,3,4,5,6,7,8,9]
paresVinteCinquenta = [n for n in range(20, 51) if n % 2 == 0]
quadrados = [num ** 2 for num in nums]
divisiveisPorSete = [n for n in range(1, 100) if n % 7 == 0]
ParImpar = ["Ímpar" if n % 2 != 0 else "Par" for n in range(0, 30, 3)]
print("Pares entre 20 e 50:", paresVinteCinquenta)
print("Quadrados dos números de 1 a 9:", quadrados)
print("Números entre 1 e 100 divisíveis por 7:", divisiveisPorSete)
print("Pares e ímpares no conjunto (0, 30, 3)", ParImpar)