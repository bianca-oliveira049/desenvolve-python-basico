with open ('meus_livros.csv', 'a') as planilha:
    planilha.write('Título,Autor,Ano de publicação,Número de páginas\n')
    for i in range(10):
        linha = input("Escreva as informações do livro (Título,Autor,Ano de publicação,Número de páginas):")
        linha = linha.split(',')
        planilha.write(','.join(linha) + '\n')

    
    