def questao1_v1_concatenar_strings(lista_1,lista_2):
    """
    cria uma lista que cada indice é a concatenação de um mesmo indice

    Argumento:
    Duas listas de string

    retorno:
    Uma lista de string
    """
    lista = []
    for x,y in zip(lista_1,lista_2):
        lista.append(x + y)
    return lista

def questao1_v2_concatenar_strings(lista_1,lista_2):
    """
    cria uma lista que cada indice é a concatenação de um mesmo indice

    Argumento:
    Duas listas de string

    retorno:
    Uma lista de string
    """
    return [x + y for x,y in zip(lista_1,lista_2)]
#///////////////////////////////////////////////////////////////

def eh_primo(item):
    for divisor in range(2,item):
        if item % divisor == 0:
            return False
    return True
def calcular_proximo_primo(item):
    item += 1
    while not eh_primo(item):
        item += 1
    return item

def construir_lista_primos(lista):
    """
    constroe um lista de numeros primos apartir de uma lista de inteiros
    Argumento:
    uma lista de inteiro

    retorno:
    uma lista de primos
    """
    return [calcular_proximo_primo(item)\
            for item in lista]
#///////////////////////////////////////////////////////////////

def questao_3_v1_menor_10(lista_string):
    """
    Organiza uma lista de strings em palavras menores que 10 em ordem alfabética

    Argumento:
    uma lista de string

    retorno:
    uma lista de string
    """
    lista  = []
    for item in lista_string:
        if len(item) < 10:
            lista.append(item)
    return sorted(lista)

def questao_3_v2_menor_10(lista_string):
    """
    Organiza uma lista de strings em palavras menores que 10 em ordem alfabética

    Argumento:
    uma lista de string

    retorno:
    uma lista de string
    """
    return sorted([item
        for item in lista_string\
             if len(item) < 10])
#///////////////////////////////////////////////////////////////
