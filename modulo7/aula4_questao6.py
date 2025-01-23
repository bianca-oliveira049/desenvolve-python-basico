with open ('spotify-2023.csv', 'r', encoding='latin-1') as arq:
    linhas = arq.readlines()
    ano = 2012
    listaMaisTocadas = []
    while ano < 2022:
        listaFiltradaAno = []
        linhaMaisTocada = -1
        for i in range(len(linhas)):
            if i == 0: continue
            colunas = linhas[i].strip().split(',')
            if len(colunas) > 8:
                try:
                    if int(colunas[3]) == ano and (not colunas[0].startswith('"') and not colunas[1].startswith('"')):
                        listaFiltradaAno.append(colunas)
                except ValueError: continue
        for i in range(len(listaFiltradaAno)):
            try:
                if int(listaFiltradaAno[i][8]) > int(listaFiltradaAno[linhaMaisTocada][8]):
                    linhaMaisTocada = i
            except ValueError: continue
        listaMaisTocadas.append(listaFiltradaAno[linhaMaisTocada][0:3:] + [listaFiltradaAno[linhaMaisTocada][8]])
        ano += 1
    for linha in listaMaisTocadas:
        print(linha)
