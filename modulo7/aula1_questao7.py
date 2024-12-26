def encrypt():
    tam = int(input("Digite a quantidade de strings da lista: "))
    chave_aleatoria = int(input("Digite o valor da chave aleatória: "))
    lista = []
    criptografados = []
    for i in range(tam): lista.append(input("Digite o item da lista: "))
    for item in lista:
        aux = item
        string = ''
        for letra in aux:
            letra = chr(ord(letra) + chave_aleatoria)
            string += letra
        item = string
        criptografados.append(item)
    print(criptografados)
encrypt()