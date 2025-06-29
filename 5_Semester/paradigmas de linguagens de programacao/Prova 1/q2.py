def cauda(lista):
    return lista[1:]

def cabeca(lista):
    return lista[0]

def tamanho(lista):
    if lista == []:
        return 0
    
    return 1 + tamanho(cauda(lista))

lista=[1,2,3,4]

print(tamanho(lista))
