def ler_datatran2020():
    with open('datatran2020.csv', 'r', encoding='utf-8') as f:
        data = [linha.split(',') for linha in f]
        colunas = data[0]
        bd = dict()
        for id, coluna in enumerate(colunas):
            bd[coluna] = [item[id] for item in data[1:]]
    return bd

def colunas():
    with open('datatran2020.csv', 'r', encoding='utf-8') as f:
        data = [linha.split(',') for linha in f]
        print(*data[0], sep='\n')

def questao_1():
    base = ler_datatran2020()
    lista = base['fase_dia']
    valores = set(lista)
    print(valores)

def questao_2():
    base = ler_datatran2020()
    lista = base['fase_dia']
    chaves = set(lista)
    bd = dict()
    for ch in chaves:
        bd[ch] = 0
        for item in lista:
            if item == ch:
                bd[ch] += 1
    print(bd)

def questao_3():
    base = ler_datatran2020()
    lista = base['uf']
    chaves = set(lista)
    bd = dict()
    for ch in chaves:
        bd[ch] = 0
        for item in lista:
            if item == ch:
                bd[ch] += 1
    print(bd)


questao_1()
print('-=-=-=-=-=-=-=-=-')
questao_2()
print('-=-=-=-=-=-=-=-=-')
questao_3()
print('-=-=-=-=-=-=-=-=-')
base = ler_datatran2020()
for chave in base:
    print(base[chave][:3])
