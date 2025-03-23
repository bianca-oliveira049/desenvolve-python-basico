## TRABALHO PRÁTICO - PROGRAMAÇÃO BÁSICA COM PYTHON

##Importação de bibliotecas ou funções de bibliotecas
import csv
from random import randint
from rich import print
from rich.table import Table, box

#Lê o arquivo de usuários usando um leitor e armazena cada linha em uma tupla. Ao final, retorna a uma lista com as tuplas
def leituraUsuarios():
    with open ('usuarios.csv', 'r', encoding='utf-8') as arqUsuarios:
        leitorUsuarios = csv.reader(arqUsuarios)
        usuarios = []
        for linha in leitorUsuarios:
            if len(tuple(linha)) == 3: usuarios.append(tuple(linha))
        usuarios = usuarios[1:]
    return usuarios

#Lê o arquivo de produtos usando um leitor e armazena cada linha em uma tupla. Ao final, retorna a uma lista com as tuplas
def leituraProdutos():
    with open ('produtos.csv', 'r', encoding='utf-8') as arqProdutos:
        leitorProdutos = csv.reader(arqProdutos)
        produtos = []
        for linha in leitorProdutos:
            if len(tuple(linha)) == 3: produtos.append(tuple(linha))
        produtos = produtos[1:]
    return produtos
        
## MENU DE OPÇÕES INICIAL (CADASTRO, LOGIN OU SAIR)
#Exibe um menu inicial, recebe a entrada do usuário e a retorna quando for válida
def menuInicial():
    print("[bold underline #FA7F08]Menu inicial[/bold underline #FA7F08]\n")
    while True:
        print("[bold]Escolha uma das opções abaixo:[/bold]")
        op = int(input("\n1 - Cadastro\n2- Login\n3 - Sair\n\n-> "))
        if not (op == 1 or op == 2 or op == 3): 
            print("[red]Opção inválida![/red]\n")
        else: break
    return op

## MENU DE TIPOS DE USUÁRIO
#No caso de cadastro, o usuário seleciona o tipo de usuário que será cadastrado e a função retorna a opção escolhida
def tiposUsuario():
    tipo = None
    while not tipo:
        op = int(input("Indique o tipo de usuário:\n1 - Cliente\n2 - Funcionário\n3 - Gerente\n\n-> "))
        if op == 1: tipo = 'Cliente'
        elif op == 2: tipo = 'Funcionário'
        elif op == 3: tipo = 'Gerente'
        else: print("[red]Opção inválida![/red]")
    return tipo

## MENU DE OPÇÕES FUNCIONÁRIO
## MENU DE OPÇÕES CLIENTE

## CRUD DE USUÁRIOS

## Entrada e validação de senha
#A função faz a entrada da senha e confirmação de senha, quando as duas entradas forem iguais, retorna a senha criada
def entradaSenha():
    confirma = False
    while not confirma:
        senha = input("Crie uma senha: ")
        confirmaSenha = input("Confirme a senha: ")
        if senha == confirmaSenha: 
            confirma = True
            return senha
        else:
            print("[red]Digite a mesma senha nos dois campos![/red]")
        
## Read
#A função que recebe o nome de um usuário e procura o nome na lista recebida pela função de leitura. Ao final retorna a linha i que corresponder ao nome do usuário
#Se o usuário não existir retorna Falso
def procuraUsuario(nomeUsuario):
    usuarios = leituraUsuarios()
    for i in range(len(usuarios)):
        if str(usuarios[i][0]).lower() == str(nomeUsuario).lower(): return i
    return False

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Create
## Cadastro de usuário
#Recebe as entradas de nome, invoca as funções tipoUsuario() e entradaSenha() para que sejam preenchidos os campos de tipo e senha. Abre o arquivo de usuários e escreve 
#a nova linha a partir de uma tupla com os dados cadastrados
def cadastraUsuario():
    nome = input("Digite o nome: ")
    tipo = tiposUsuario()
    senha = entradaSenha()
    dadosCadastro = nome, tipo, senha
    if type(procuraUsuario(nome)) == int:
        with open ('usuarios.csv', 'a', newline='', encoding='utf-8') as usuarios:
            escritor = csv.writer(usuarios)
            escritor.writerow(dadosCadastro)
            print("[green]Cadastro realizado com sucesso![/green]\n")
    else: print("[red]Esse usuário já existe![/red]")
        
## Login de usuário
#A função chama a função de leitura do arquivo de usuários, recebe os dados de nome e senha do usuário que está tentando logar. Caso o usuário exista e a senha esteja
#correta, é exibida uma mensagem de boas-vindas e é retornado o nome do usuário logado. Caso contrário, o processo se inicia novamente
def login():
    usuarios = leituraUsuarios()
    while True:
        nome = input("Digite seu nome: ")
        linha = procuraUsuario(nome)
        if type(linha) == int:
            senha = input("Digite sua senha: ")
            if senha == usuarios[linha][2]:
                print(f"\n[green]Seja bem-vindo(a) {usuarios[linha][0]}[/green]")
                return nome
            else: print("[red]Senha incorreta![/red]")
        else: 
            print("[red]Usuário não existe![/red]")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
##Listagem de usuários
#Recebe os dados do arquivo de usuários, e cria uma tabela a partir da biblioteca rich, cada item da lista é colocado como uma linha da tabela, que ao final é 
#exibida na tela
def listaUsuarios():
    usuarios = leituraUsuarios()
    tabelaUsuarios = Table(title="Usuários", box=box.DOUBLE_EDGE)
    tabelaUsuarios.add_column('Nome')
    tabelaUsuarios.add_column('Tipo')
    for usuario in usuarios:
        if len(usuario) == 3:
            nome, tipo, senha = usuario
            tabelaUsuarios.add_row(nome, tipo)
    print(tabelaUsuarios)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Update
##Atualiza cadastro de usuário
#Recebe o nome do usuário que terá seu cadastro atualizado, chama a função de leitura de usuários e armazena o retorno em uma variável, chama a função de procura
#de usuário e armazena seu retorno em uma variável 'linha'. O usuário seleciona se deseja alterar nome ou senha. Ao final, é feita a alteração na lista de usuários 
#e o arquivo de usuários é sobrescrito com a atualização feita.
def atualizaCadastro(nomeUsuario):
    usuarios = leituraUsuarios()
    linha = procuraUsuario(nomeUsuario)
    nome, tipo, senha = usuarios[linha]
    while True:
        op = int(input("Indique qual dado gostaria de atualizar:\n1 - Nome\n2 - Senha\n\n-> "))
        if op == 1:
            novoDado = input("Digite o novo nome: ")
            usuarios[linha] = (novoDado, tipo, senha)
            break
        elif op == 2: 
            print("Crie uma nova senha")
            novoDado = entradaSenha()
            usuarios[linha] = (nome, tipo, novoDado)
            break
        else: print("[red]Opção inválida![/red]")
    with open ('usuarios.csv', 'w', newline='', encoding='utf-8') as arqUsuarios:
        escritor = csv.writer(arqUsuarios)
        escritor.writerow(tuple(('Nome,Tipo,Senha').split(',')))
        escritor.writerows(usuarios)
    print("[green]Cadastro atualizado com sucesso![/green]")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Delete
##Remoção de usuário
#Recebe o nome do usuário que será deletado, e procura a linha em que ele se encontra. Armazena o valor de 'linha' e caso seja tipo int, deleta a tupla
#correspondente da lista de usuários e sobrescreve o arquivo com o usuário já deletado. Se o usuário foi deletado, exibe uma mensagem de confirmação, caso contrário
#indica que o usuário não foi encontrado
def deletaUsuario():
    nome = input("Digite o nome do usuário que deseja deletar: ")
    linha = procuraUsuario(nome)
    usuarios = leituraUsuarios()
    if type(linha) == int:
            del usuarios[linha]
            with open ('usuarios.csv', 'w', newline='', encoding='utf-8') as arqUsuarios:
                escritor = csv.writer(arqUsuarios)
                escritor.writerow(tuple(('Nome,Tipo,Senha').split(',')))
                escritor.writerows(usuarios)
                print("[green]Usuário deletado com sucesso![/green]")
    else: print("[red]Usuário não encontrado![red]")

#--------------------------------------------------------------------------------------------------------------------------------    

## CRUD PRODUTOS
##Imprime os produtos ordenados por nome
#recebe a lista de produtos através da função leituraProdutos() e a armazena. Ordena as tuplas pelo nome dos produtos e adiciona os dados em uma tabela que será
#exibida ao final da função
def produtosOrdenadosNome():
    produtos = leituraProdutos()
    produtos = sorted(produtos)
    tabelaProdutos = Table(title="Produtos ordenados por preço", box=box.DOUBLE_EDGE)
    tabelaProdutos.add_column('Produto')
    tabelaProdutos.add_column('Código')
    tabelaProdutos.add_column('Preço')
    for produto in produtos:
        nome, codigo, preco = produto
        tabelaProdutos.add_row(nome, codigo, preco)
    print(tabelaProdutos)

##Imprime os produtos ordenados por preço
#recebe a lista de produtos através da função leituraProdutos() e a armazena. Ordena as tuplas a partir de uma função lambda que retorna o terceiro elemento (preço)
#e adiciona os dados em uma tabela que será exibida ao final da função
def produtosOrdenadosPreco():
    produtos = leituraProdutos()
    produtos = sorted(produtos, key = lambda produto: float(produto[2]))
    tabelaProdutos = Table(title="Produtos ordenados por nome", box=box.DOUBLE_EDGE)
    tabelaProdutos.add_column('Produto')
    tabelaProdutos.add_column('Código')
    tabelaProdutos.add_column('Preço')
    for produto in produtos:
        nome, codigo, preco = produto
        tabelaProdutos.add_row(nome, codigo, preco)
    print(tabelaProdutos)   

#Pede ao usuário para escolher entre ordenação por nome do produto ou preço. Caso o usuário digite uma opção válida, executa a função correspondente 
def escolhaOrdenacaoProdutos():
    while True:
        tipoOrdenacao = int(input("Escolha uma opção\n1 - Listar produtos ordenados por nome\n"
            "2 - Listar produtos ordenados por preço\n\n-> "))
        if tipoOrdenacao == 1: 
            produtosOrdenadosNome()
            break
        elif tipoOrdenacao == 2: 
            produtosOrdenadosPreco()
            break
        else: 
            print("[red]Opção inválida![/red]")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------            

## Read
##Busca por nome do produto
#O parãmetro é nome do produto a ser buscado, armazena o retorno da função de leitura dos produtos em uma variável e através de um laço procura uma correspondência
#entre o nome na linha i e o nome buscado. Caso o produto exista, a função retorna a linha do produto, caso contrário retorna Falso
def procuraProdutoNome(nomeProduto):
    produtos = leituraProdutos()
    for i in range(len(produtos)):
        if str(produtos[i][0]).lower() == str(nomeProduto).lower(): return i
    return False

##Busca por código do produto
#O parâmetro é o código do produto a ser buscado, armazena o retorno da função de leitura dos produtos em uma variável e através de um laço procura uma correspondência
#entre o  na código da linha i e o código buscado. Caso o produto exista, a função retorna a linha do produto, caso contrário retorna Falso
def procuraProdutoCodigo(codigo):
    produtos = leituraProdutos()
    for i in range(len(produtos)):
        if produtos[i][1] == codigo: return i
    return False

#Pede ao usuário que escolha entre as formas de busca de produto disponíveis. Se a entrada for válida, executa a função correspondente e retorna a linha caso o produto
#exista
def escolhaBuscaProduto():
    while True:
        formaBusca = int(input("Escolha uma opção\n1 - Procurar produto por nome\n2 - Procurar produto por código\n\n-> "))
        if formaBusca == 1: 
            nome = input("Digite o nome do produto que deseja procurar: ")
            linha = procuraProdutoNome(nome)
        elif formaBusca == 2: 
            codigo = input("Digite o código do produto que deseja buscar: ")
            linha = procuraProdutoCodigo(codigo)
        else: 
            print("[red]Opção inválida![/red]")
            continue
        if type(linha) == int: return linha
        else: print("[red]Produto não encontrado![/red]")
        break
        
#--------------------------------------------------------------------------------------------------

## Create
#Recebe do usuário o nome e o preço. Caso o produto ainda não exista e o preço seja válido, é gerado o código do produto a partir de um valor aleatório que ao final
#terá 3 dígitos. Por fim, abre o arquivo de produtos e escreve a nova linha a partir de uma tupla com os dados do produto
def cadastraProduto():
    while True:
        nomeProduto = input("Digite o nome do produto: ")
        if  type(procuraProdutoNome(nomeProduto)) == bool:
            preco = float(input("Digite o preço do produto: "))
            if preco <= 0: 
                print("[red]Preço inválido, digite um valor positivo![/red]")
            else: 
                break
        else: print("[red]Esse produto já existe![/red]")
    while True:            
        codigo = str(randint(1, 999))
        if len(codigo) < 3:
            codigo = ((3 - len(codigo)) * '0') + codigo
        if type(procuraProdutoCodigo(codigo)) == bool: break
    dadosProduto = nomeProduto, codigo, preco
    with open ('produtos.csv', 'a', newline='', encoding='utf-8') as arqProdutos:
        escritor = csv.writer(arqProdutos)
        escritor.writerow(dadosProduto) 
    print("[green]Produto cadastrado com sucesso![/green]")
            
#-------------------------------------------------------------------------------------------------

## Update
##Atualizar o preço do produto
#Recebe o retorno da função de leitura dos produtos, chama a função de busca para obter a linha do produto, desenpacota a tupla correspondente, recebe o novo preço
#e substitui a tupla antiga pela tupla atualizada. Por fim, sobrescreve os dados no arquivo
def atualizaPrecoProduto():
    produtos = leituraProdutos()
    while True:
        linha = escolhaBuscaProduto()
        if type(linha) == bool: print("[red]Esse produto não existe![/red]")
        else:
            nome, codigo, preco = produtos[linha]
            novoPreco = float(input("Digite o novo preço do produto: "))
            if novoPreco <= 0: 
                print("[red]Preço inválido, digite um valor positivo![/red]")
                continue
            novoPreco = f"{round(novoPreco, 2):,.2f}"
            produtos[linha] = (nome, codigo, novoPreco)
            with open ('produtos.csv', 'w', newline='', encoding='utf-8') as arqProdutos:
                escritor = csv.writer(arqProdutos)
                escritor.writerow(tuple(('Nome,Codigo,Preço').split(',')))
                escritor.writerows(produtos)
            print("[green]Preço atualizado com sucesso![/green]")
        break

#--------------------------------------------------------------------------------------------------------------------------------

## Delete
##Remoção de produto
#Chama a função de leitura dos produtos, encontra a linha do produto a ser removido a partir da função de busca, remove a tupla correspondente ao produto da lista,
#e sobrescreve o arquivo já sem a linha removida
def deletarProduto():
    produtos = leituraProdutos()
    while True:
        linha = escolhaBuscaProduto()
        if linha: break
        else: print("[red]Esse produto não existe![/red]")
    del produtos[linha]
    with open ('produtos.csv', 'w', newline='', encoding='utf-8') as arqProdutos:
        escritor = csv.writer(arqProdutos)
        escritor.writerow(tuple(('Nome,Codigo,Preço').split(',')))
        escritor.writerows(produtos)
    print("[green]Produto deletado com sucesso![/green]")

#--------------------------------------------------------------------------------------------------------------------------------    

## FUNÇÕES PARA EXECUÇÃO DAS FUNÇÕES ANTERIORES DE ACORDO COM O TIPO DE USUÁRIO
#As três funções abaixo recebem como parâmetro o nome do usuário logado, apresentam o menu correspondente ao tipo de usuário logado, recebem a opção escolhida e,
#caso a entrada seja válida, executam a função escolhida. No caso de busca de produto/usuário, há recebimento da linha em que o produto/usuário se encontra, para
#então exibir os atributos. Se o usuário optar por 'Sair', a função chega ao fim
def executaFuncoesGerente(nomeGerente):
    while True:
        usuarios = leituraUsuarios()
        produtos = leituraProdutos()
        op = int(input("\nEscolha uma opção\n1 - Cadastrar produto\n2 - Listar produtos\n3 - Procurar produto\n"
        "4 - Atualizar produto\n5 - Deletar produto\n6 - Listar usuários\n7 - Procurar usuário\n8 - Atualizar cadastro\n9 - Deletar usuário\n10 - Sair\n\n-> "))
        if op == 1: cadastraProduto()
        elif op == 2: escolhaOrdenacaoProdutos()
        elif op == 3: 
            linhaProd = escolhaBuscaProduto()
            if type(linhaProd) == int:
                nomeProd, codigo, preco = produtos[linhaProd]
                print(f"[bold #FA7F08]Nome:[/] {nomeProd}\n[bold #FA7F08]Código:[/] {codigo}\n[bold #FA7F08]Preço:[/] {preco}\n")
        elif op == 4: atualizaPrecoProduto()  
        elif op == 5: deletarProduto()
        elif op == 6: listaUsuarios()
        elif op == 7: 
            nome = input("Digite o nome do usuário que deseja procurar: ")
            linha = procuraUsuario(nome)
            if type(linha) == int: 
                nomeUsuario, tipo, senha = usuarios[linha]
                print(f"[bold #FA7F08]Nome:[/] {nomeUsuario}\n[bold #FA7F08]Tipo:[/] {tipo}\n")
            else: print("\n[red]Usuário não encontrado![/red]\n")
        elif op == 8: atualizaCadastro(nomeGerente)
        elif op == 9: deletaUsuario()
        elif op == 10: 
            print("[blue]Saindo...[/blue]")
            break
        else: print("[red]Opção inválida![/red]")

def executaFuncoesFuncionario(nomeFuncionario):
    while True:
        produtos = leituraProdutos()
        op = int(input("\nEscolha uma opção:\n1 - Cadastrar produto\n2 - Listar produtos\n3 - Procurar produto\n"
            "4 - Atualizar produto\n5 - Deletar produto\n6 - Atualizar cadastro\n7 - Sair\n\n-> "))
        if op == 1: cadastraProduto()
        elif op == 2: escolhaOrdenacaoProdutos()
        elif op == 3: 
            linhaProd = escolhaBuscaProduto()
            if type(linhaProd) == int:
                nomeProd, codigo, preco = produtos[linhaProd]
                print(f"[bold #FA7F08]Nome:[/] {nomeProd}\n[bold #FA7F08]Código:[/] {codigo}\n[bold #FA7F08]Preço:[/] {preco}\n")
        elif op == 4: atualizaPrecoProduto()
        elif op == 5: deletarProduto()
        elif op == 6: atualizaCadastro(nomeFuncionario)
        elif op == 7: 
            print("[blue]Saindo...[/blue]")
            break
        else: print("[red]Opção inválida![/blue]")

def executarFuncoesCliente(nomeCliente):
    while True:
        produtos = leituraProdutos()
        op = int(input("\nEscolha uma opção:\n1 - Procurar produto\n2 - Listar produtos\n3 - Atualizar cadastro\n4 - Sair\n\n-> "))
        if op == 1: 
            linhaProd = escolhaBuscaProduto()
            if type(linhaProd) == int:
                nomeProd, codigo, preco = produtos[linhaProd]
                print(f"[bold #FA7F08]Nome:[/] {nomeProd}\n[bold #FA7F08]Código:[/] {codigo}\n[bold #FA7F08]Preço:[/] {preco}\n")
        elif op == 2: escolhaOrdenacaoProdutos()
        elif op == 3: atualizaCadastro(nomeCliente)
        elif op == 4:
            print('[blue]Saindo...[/blue]')
            break
        else: print("[red]Opção inválida![/red]")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------        

## PROGRAMA PRINCIPAL
#É exibido o menu inicial e a função correspondente à opção escolhida é executada. Caso seja executada a função de login, há uma variável que recebe o nome retornado
#e a partir dele há uma busca pelo usuário, do qual será identificado o tipo, para que seja executada a função condizente com o tipo de usuário. Se o usuário opta por
#'Sair', o programa é finalizado
if __name__ == "__main__":
    while True:
        op = menuInicial()
        if op == 1: 
            cadastraUsuario()
            continue
        elif op == 2: 
            nomeUsuario = login()
            if nomeUsuario:
                linha = procuraUsuario(nomeUsuario)
                usuarios = leituraUsuarios()
                if usuarios[linha][1] == 'Gerente': executaFuncoesGerente(nomeUsuario)
                elif usuarios[linha][1] == 'Funcionário': executaFuncoesFuncionario(nomeUsuario)
                else: executarFuncoesCliente(nomeUsuario)
        else:
            print("\n[blue]Saindo...[/blue]\n")
            break
