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

def questao_4_lista_homogenea(lista_heterogenea):
    """
    Organiza uma lista de strings em palavras menores que 10 em ordem alfabética

    Argumento:
    uma lista com varias listas

    retorno:
    uma lista de lista de inteiro
    """
    lista_homogenea = []
    count = 0
    for item in lista_heterogenea:
        for i in item:
            if type(i) == int:
                count += 1
        if count == len(item):
            lista_homogenea.append(item)
    return lista_homogenea

def questao_5_v1_lista_de_string_com_correspondecia_a_uma_lista_de_inteiros(lista_de_string, lista_de_inteiros):
    """
    Organiza uma lista de string de acordo com o tamanho de cada elemento de uma outra lista de inteiros

    Argumento:
    uma lista de string e uma lista de inteiros

    retorno:
    uma lista de lista de string
    """
    lista_de_string_filtrada = []
    for item in zip(lista_de_string,lista_de_inteiros):
        if len(item[0]) <= item[1]:
            lista_de_string_filtrada.append(item[0])
    return lista_de_string_filtrada

def questao_5_v2_lista_de_string_com_correspondecia_a_uma_lista_de_inteiros(lista_de_string, lista_de_inteiros):
    """
    Organiza uma lista de string de acordo com o tamanho de cada elemento de uma outra lista de inteiros

    Argumento:
    uma lista de string e uma lista de inteiros

    retorno:
    uma lista de lista de string
    """
    return [item[0] for item in zip(lista_de_string,lista_de_inteiros) if len(item[0]) <= item[1] ]

def questao_6_v1_lista_de_lista_de_string_com_proximo_numero_maior_que_o_inteiro(lista_de_lista_de_inteiro):
    count_lista_1 = 0
    count_lista_2 = 0
    for item in lista_de_lista_de_inteiro:
        for num in item:
            count_lista_1 += num

def questao_7_v1_reducao_para_encontrar_a_menor_soma_resultante(lista_inteiros_1,lista_inteiros_2,lista_inteiros_3):
    """
    Dada três lista de números inteiros, faça uma redução para encontrar o
menor número resultante da soma dos elementos de índices correspondentes. Retorne
o valor encontrado

    Argumento:
    Tres listas de inteiros

    retorno:
    um numero inteiro
    """
    lista_resultante = []
    for numbers in zip(lista_inteiros_1,lista_inteiros_2,lista_inteiros_3):
        lista_resultante.append(numbers[0] + numbers[1] + numbers[2])
    return min(lista_resultante)

def questao_7_v2_reducao_para_encontrar_a_menor_soma_resultante(lista_inteiros_1,lista_inteiros_2,lista_inteiros_3):
    """
    Dada três lista de números inteiros, faça uma redução para encontrar o
menor número resultante da soma dos elementos de índices correspondentes. Retorne
o valor encontrado

    Argumento:
    Tres listas de inteiros

    retorno:
    um numero inteiro
    """
    lista_resultante = [numbers[0] + numbers[1] + numbers[2] for numbers in zip(lista_inteiros_1, lista_inteiros_2, lista_inteiros_3)]
    return min(lista_resultante)

def questao_8_v1_encontrar_maior_string(lista):
    """
    Dada uma lista de string, faça uma redução para determinar o tamanho da
    maior string. Retorne o valor encontrado e o índice correspondente na lista. Se mais de
    uma string possuir o maior tamanho, retorne o menor índice.


    Argumento:
    Tres listas de string

    retorno:
    um numero inteiro e o indice
    """
    maior_tamanho = 0
    menor_indice = float('inf')
    indice_maior_string = None

    for i, string in enumerate(lista):
        tamanho_atual = len(string)
        
        if tamanho_atual > maior_tamanho:
            maior_tamanho = tamanho_atual
            menor_indice = i
            indice_maior_string = i
        elif tamanho_atual == maior_tamanho and i < menor_indice:
            menor_indice = i
            indice_maior_string = i

    return maior_tamanho, indice_maior_string

def questao_8_v2_encontrar_maior_string(lista):
    """
    Dada uma lista de string, faça uma redução para determinar o tamanho da
    maior string. Retorne o valor encontrado e o índice correspondente na lista. Se mais de
    uma string possuir o maior tamanho, retorne o menor índice.

    Argumento:
    Uma lista de string

    retorno:
    Um número inteiro e o índice
    """
    maior_tamanho = max(len(string) for string in lista)
    indice_maior_string = min(i for i, string in enumerate(lista) if len(string) == maior_tamanho)

    return maior_tamanho, indice_maior_string

def questao_9_v1_somar_numeros_de_uma_lista(lista):
    """
    Dada uma lista de números reais, faça uma redução que implique na soma
    dos elementos. O elemento da posição i só pode ser somado se ele for maior que o
    elemento da posição i+1. Retorne o valor encontrado.

    Argumento:
    Uma lista de inteiros

    retorno:
    Um número inteiro
    """
    soma = 0
    for numero in range(len(lista) - 1):
        if lista[numero] > lista[numero + 1]:
            soma += lista[numero]
    return soma

def questao_9_v2_somar_numeros_de_uma_lista(lista):
    """
    Dada uma lista de números reais, faça uma redução que implique na soma
    dos elementos. O elemento da posição i só pode ser somado se ele for maior que o
    elemento da posição i+1. Retorne o valor encontrado.

    Argumento:
    Uma lista de inteiros

    retorno:
    Um número inteiro
    """
    return sum([lista[numero] for numero in range(len(lista) - 1) if lista[numero] > lista[numero + 1]])

def questao_10_v1_concatena_de_string(lista_strings):
    """
    Dada uma lista de string, faça uma redução que resulte em uma string
    concatenando todos os elementos separados por vírgula e espaço em branco. Retorne
    o valor encontrado.

    Argumento:
    Uma lista de string

    retorno:
    Uma string
    """
    palavra_concatenada = ''
    for palavra in lista_strings:
        palavra_concatenada += palavra.strip() + ", "
    return palavra_concatenada

def questao_10_v2_concatena_de_string(lista_strings):
    """
    Dada uma lista de string, faça uma redução que resulte em uma string
    concatenando todos os elementos separados por vírgula e espaço em branco. Retorne
    o valor encontrado.

    Argumento:
    Uma lista de string

    retorno:
    Uma string
    """
    return ', '.join([palavra.strip() for palavra in lista_strings ])

