def cauda(lista):
    return lista[1:]

def cabeca(lista):
    return lista[0]


def maior(lista):
    if not lista:
        return None
    
    if len(lista) == 1:
        return cabeca(lista)
    
    max = maior(cauda(lista))

    if cabeca(lista) > max:
        return cabeca(lista)
    else:
        return max
    
lst = [2, 1, 4, 3]
print(maior(lst)) 