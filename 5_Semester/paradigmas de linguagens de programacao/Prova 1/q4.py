def cauda(lista):
    return lista[1:]

def cabeca(lista):
    return lista[0]

def posicao(lista, x):
    if not lista:
        return -1
    
    if cabeca(lista) == x:
        return 0
    
    posicao(cauda(lista), x)

    if posicao(cauda(lista), x) == -1:
        return -1
    else:
        return posicao(cauda(lista), x) + 1
    
lista = [1,2,3,4]

print(posicao(lista, 4))