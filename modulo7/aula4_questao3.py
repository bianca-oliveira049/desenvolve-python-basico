maiorLinha = 0
nonato = 0
iria = 0
with open ('C:\\Users\\PDITA049\\OneDrive\\Desktop\\estomago.txt', 'r') as roteiro:
    linhas = roteiro.readlines()
    for i in range(len(linhas)):
        if i <= 24: print(linhas[i])
        if len(linhas[i]) > len(linhas[maiorLinha]): maiorLinha = i
        nonato += linhas[i].lower().count('nonato')
        iria += linhas[i].lower().count('íria')
print(f"Número de linhas: {i}")
print(f"Maior linha: {linhas[maiorLinha]}")
print(f"Número de ocorrências do nome Nonato: {nonato}")
print(f"Número de ocorrências do nome Íria: {iria}")


        