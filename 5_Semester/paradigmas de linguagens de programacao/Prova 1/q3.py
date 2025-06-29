def cauda(lista):
    return lista[1:]

def cabeca(lista):
    return lista[0]

def estaPresente(lista, x):
    if lista == []:
        return False
    
    if cabeca(lista) == x:
        return True
    
    return estaPresente(cauda(lista), x)

lista=[1,2,3,4]

print(estaPresente(lista,2))