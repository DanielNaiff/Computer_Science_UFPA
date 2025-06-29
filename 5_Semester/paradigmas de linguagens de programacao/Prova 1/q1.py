def cauda(lista):
    return lista[1:]

def cabeca(lista):
    return lista[0]

def soma(lista):
    if lista == []:
        return 0
    
    return cabeca(lista) + soma(cauda(lista))

lista=[1,2,3,4]

print(soma(lista))