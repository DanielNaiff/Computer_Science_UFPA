def cabeca(lista):
    return lista[0] 

def cauda(lista):
    return lista[1:] 

def tamanho(lista):
    if lista == []:
        return 0
    else:
        return tamanho(cauda(lista)) + 1

def soma(lista):
    if tamanho(lista) == 0:
        return 0
    else:
        return cabeca(lista) + soma(cauda(lista))

def menor2(x, y):
    if x < y:
        return x
    else:
        return y

def menor(l):
    if tamanho(l) == 1:
        return cabeca(l)
    else:
        m = menor(cauda(l))
        return menor2(cabeca(l), m)

def retElem(l, x): 
    if x == cabeca(l):
        return cauda(l)
    else:
        resto = retElem(cauda(l), x)
        return [cabeca(l)] + resto

def selecao(l):
    if not l:
        return []
    else:
        m = menor(l)
        resto = retElem(l, m)
        return [m] + selecao(resto)

print(selecao([4, 2, 1, 7, 6]))
