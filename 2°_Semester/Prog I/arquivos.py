def menu():
    escolha = int(input('Digite 1 para cadastrar\nDigite 2 para listar\nDigite 3 para buscar um nome'))
    return escolha

def cadastrar():
    nome = input('Digite o seu nome: ')
    telefone = input('Digite o seu número: ')
    email = input('Digite o seu email:')
    with open('arquivo.txt', 'a', encoding="utf-8") as f:
        f.write(f"{nome}, {telefone}, {email}")
        f.write('\n')
    return 

def listar():
    with open('arquivo.txt', 'r', encoding="utf-8") as f:
        conteudo = f.read()
        print(conteudo)

def busca():
    lista = []
    busca = input('Digite um nome de busca')
    with open('arquivo.txt', 'r', encoding="utf-8") as f:
        for nome in f:
            if nome.startswith(busca):
                lista.append(nome)
    print(sorted(lista))
    return

def main():
    while True:
        op = menu()
        if op == 1:
            cadastrar()
        elif op == 2:
            listar()
        elif op == 3:
            busca()
        else:
            break
main()
