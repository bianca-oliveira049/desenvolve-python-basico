from random import choice

def imprime_enforcado(estagios, i):
    for parte in estagios[i]:
        print(parte)

with open ('gabarito_forca.txt', 'r') as forca:
    palavras = forca.readlines()
    palavra = choice(palavras).strip().lower()
    print(palavra)
    with open ('gabarito_enforcado.txt', 'r') as arqEnforcado:
        enforcado = arqEnforcado.readlines()
        estagiosEnforcado = []
        j = 0
        for i in range(7):
            estagio = []
            while len(estagio) < 5 and j < 78:
                if enforcado[j].strip():
                    estagio.append(enforcado[j])
                j += 1
            estagiosEnforcado.append(estagio)
        palavraUnderscore = list('_' * len(palavra))
        erros = 0
        while erros < 6:
            print(''.join(palavraUnderscore))
            if '_' not in ''.join(palavraUnderscore): 
                print("Você ganhou!")
                break
            letra = input("\nDigite uma letra: ")
            if letra in palavra:
                for k in range(len(palavra)):
                    if letra == palavra[k]: palavraUnderscore[k] = letra
            else:
                erros += 1
                imprime_enforcado(estagiosEnforcado, erros)
        if erros == 6: print("Você perdeu!")
            
            
