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
    return ', '.join([palavra.strip() for palavra in lista_strings])

def questao_11_v1_retorna_indice_maior_primo(lista_inteiros):
    indice_primo = 0
    maior_primo = 0
    for numero in range(len(lista_inteiros)):
        if eh_primo(lista_inteiros[numero]):
            if numero == 0:
                maior_primo = numero
            else:
                if lista_inteiros[numero] > maior_primo:
                    maior_primo = lista_inteiros[numero]
                    indice_primo = numero
        else:
            indice_primo = -1
    return indice_primo

def questao_12_v1_desvio_padrao(lista_reais):
    """
    Dada uma lista de números reais, faça uma redução para calcular o desvio
    padrão. Retorne o valor encontrado.

    Argumento:
    Uma lista de reais

    retorno:
    Um numero real
    """
    lista_desvio = []
    soma_desvio = 0
    media = sum(lista_reais)/len(lista_reais)
    for numero in lista_reais:
        lista_desvio.append(abs(numero - media))
    for desvio in lista_desvio:
        soma_desvio += desvio**2
    variancia = soma_desvio/len(lista_reais)
    return variancia**0.5

def questao_13_v1_busca_linear_desordenada(lista_inteiros, numero_procurado):
    """
    Dada uma lista de números inteiros, e um número a ser buscado. Crie uma
    função que faça uma busca linear do elemento e retorne quantas comparações foram
    necessárias, bem como true ou false para informar se a busca foi realizada com sucesso
    ou não.

    Argumento:
    Uma lista de inteiros, inteiro

    retorno:
    Um valor booleano e um numero inteiro
    """
    comparacoes = 0
    for numero in lista_inteiros:
        comparacoes += 1
        if numero == numero_procurado:
            return comparacoes, True
        else:
            if comparacoes == len(lista_inteiros):
                return comparacoes, False

def questao_14_v1_busca_linear_ordenada(lista_inteiros, numero_procurado):
    """
    Dada uma lista de números inteiros, e um número a ser buscado. Crie uma
    função que faça uma busca linear do elemento e retorne quantas comparações foram
    necessárias, bem como true ou false para informar se a busca foi realizada com sucesso
    ou não.

    Argumento:
    Uma lista de inteiros, inteiro

    retorno:
    Um valor booleano e um numero inteiro
    """
    comparacoes = 0
    lista_inteiros.sort()
    for numero in lista_inteiros:
        comparacoes += 1
        if numero == numero_procurado:
            return comparacoes, True
        else:
            if comparacoes == len(lista_inteiros):
                return comparacoes, False

def questao_15_v1_buscar_binaria_inteiros(lista_inteiros, numero_procurado):
    lista_inteiros.sort()
    comparacoes = 0
    inicio = 0
    fim = len(lista_inteiros) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1

        if lista_inteiros[meio] == numero_procurado:
            return comparacoes, True
        elif lista_inteiros[meio] < numero_procurado:
            inicio = meio + 1
        else:
            fim = meio - 1

    return comparacoes, False

def questao_16_v1_buscar_binaria_inteiros(lista, alvo):
    lista_ordenada = sorted(lista)
    comparacoes = 0
    frequencia = 0

    inicio, fim = 0, len(lista_ordenada) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1

        if lista_ordenada[meio] == alvo:
            frequencia += 1
            esquerda, direita = meio - 1, meio + 1

            while esquerda >= 0 and lista_ordenada[esquerda] == alvo:
                frequencia += 1
                esquerda -= 1

            while direita < len(lista_ordenada) and lista_ordenada[direita] == alvo:
                frequencia += 1
                direita += 1

            return comparacoes, frequencia
        elif lista_ordenada[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return comparacoes, frequencia

def questao_16_v2_buscar_binaria_inteiros(lista, alvo):
    return lista.count(alvo)

def questao_17_v1_dicionario(lista):
    frequencia = {}
    for n in range(1,21):
        frequencia[n] = lista.count(n)
    return frequencia

def questao_17_v2_dicionario(lista):
    frequencias = {}
    
    for elemento in lista:
        if elemento in frequencias:
            frequencias[elemento] += 1
        else:
            frequencias[elemento] = 1
    
    return frequencias

####################################################################################################

def questao_1_v1_embalagens_fora_do_padrao(lista):
    """
    Samarone trabalha em uma empresa chamada Sociedade Brasileira dos
    Caramelos (SBC). Recentemente, devido ao elevado desperdício de
    embalagens, Samarone foi designado para inspecionar as embalagens dos
    caramelos produzidas pela SBC. Samarone recebe diariamente lotes de
    embalagens e deve verificar quantas embalagens estão fora dos padrões
    estipulados pela SBC. Para facilitar a vida do Samarone, você foi contratado
    para desenvolver um programa de computador que, dada uma lista de
    embalagens, informe quantas estão fora dos padrões estipulados pela SBC.
    Cada item da lista possui um número não negativo que diz respeito ao tamanho
    da embalagem em centímetros. Sabe-se que as embalagens menores que sete
    centímetros não são aceitas pela SBC.


    Argumento:
    Uma lista de inteiros

    retorno:
    um numero inteiro
    """
    fora_do_padrao = 0
    for embalagem in lista:
        if embalagem < 7:
            fora_do_padrao += 1
    return fora_do_padrao

def questao_1_v2_embalagens_fora_do_padrao(lista):
    """
    Samarone trabalha em uma empresa chamada Sociedade Brasileira dos
    Caramelos (SBC). Recentemente, devido ao elevado desperdício de
    embalagens, Samarone foi designado para inspecionar as embalagens dos
    caramelos produzidas pela SBC. Samarone recebe diariamente lotes de
    embalagens e deve verificar quantas embalagens estão fora dos padrões
    estipulados pela SBC. Para facilitar a vida do Samarone, você foi contratado
    para desenvolver um programa de computador que, dada uma lista de
    embalagens, informe quantas estão fora dos padrões estipulados pela SBC.
    Cada item da lista possui um número não negativo que diz respeito ao tamanho
    da embalagem em centímetros. Sabe-se que as embalagens menores que sete
    centímetros não são aceitas pela SBC.


    Argumento:
    Uma lista de inteiros

    retorno:
    um numero inteiro
    """
    return len([embalagem for embalagem in lista if embalagem < 7])

def questao_2_v1_media_aprovados(lista, media):
    """
    Renato é professor de uma escola chamada Saber Brincar Compartilhar
    (SBC). No final do ano passado, Renato aplicou um teste de nivelamento para
    todos os alunos da escola. Por serem muitos, Renato está com dificuldade em
    saber quantos alunos ficaram acima da média. Como você é amigo do Renato,
    ele pediu a sua ajuda para escrever um programa de computador que, dada
    uma lista com a nota dos alunos e o valor da média escolar da SBC, informe
    quantos alunos obtiveram a nota superior a média calculada.



    Argumento:
    Uma lista de inteiros , um numero inteiro

    retorno:
    um numero inteiro
    """
    aprovados = 0
    for nota in lista:
        if nota > media:
            aprovados += 1 
    return aprovados

def questao_2_v2_media_aprovados(lista, media):
    """
    Renato é professor de uma escola chamada Saber Brincar Compartilhar
    (SBC). No final do ano passado, Renato aplicou um teste de nivelamento para
    todos os alunos da escola. Por serem muitos, Renato está com dificuldade em
    saber quantos alunos ficaram acima da média. Como você é amigo do Renato,
    ele pediu a sua ajuda para escrever um programa de computador que, dada
    uma lista com a nota dos alunos e o valor da média escolar da SBC, informe
    quantos alunos obtiveram a nota superior a média calculada.



    Argumento:
    Uma lista de inteiros , um numero inteiro

    retorno:
    um numero inteiro
    """
    return len([ nota for nota in lista if nota > media])

def questao_3_v1_maior_altura(lista):
    """
    Marcelle é a nova professora de educação física na escola chamada Saber
    Brincar Compartilhar (SBC). Marcelle recebeu a ficha de cadastro de todos os
    seus alunos e está curiosa para saber a altura do aluno mais alto da turma.
    Como são muitos alunos, Marcelle pediu a sua ajuda para escrever um
    programa de computador que, dada a lista da altura dos alunos da professora
    Marcelle, informe qual a maior altura.


    Argumento:
    Uma lista de reais

    retorno:
    um numero real
    """
    return max(lista)

def questao_4_v1_media_numeros_pares(lista):
    lista_pares = []
    for numero in lista:
        if numero % 2 == 0:
            lista_pares.append(numero)
    return sum(lista_pares)/len(lista_pares)

def questao_5_v1_frequencia_de_bases_nitrogenadas(lista, base_alvo):
    frequencia = 0
    for base in lista:
        if base == base_alvo:
            frequencia += 1
    return frequencia

def questao_6_v1_sprint_backlog(lista,velocidade):
    complexidade  = 0
    numero_itens = 0
    for item in lista:
        complexidade += item
        numero_itens += 1
        if complexidade >= velocidade:
            return numero_itens - 1

def questao_7_v1_ordem_chegada(lista):
    count = 0
    for i  in range(len(lista)):
        if i + 1 == lista[i]:
            count += 1
    return count

def questao_8_v1_conta_conceito(lista):
    conceito_dicionario = {
        "E": 0,
        "B": 0,
        "R": 0,
        "I": 0
                        }
    for conceito in lista:
        if conceito in conceito_dicionario:
            conceito_dicionario[conceito] += 1
    return f"E = {conceito_dicionario['E']}",f"B = {conceito_dicionario['B']}",f"R = {conceito_dicionario['R']}",f"I = {conceito_dicionario['I']}"

def questao_9_v1_nivel_de_vunerabilidade(lista):
    dicionario = {
        "Muito Seguro": 0,
        "Seguro": 0,
        "Quase seguro": 0,
        "Inseguro": 0
                }
    for nivel in lista:
        if nivel == 0:
            dicionario["Muito Seguro"] += 1
        elif 1 <= nivel <= 3:
            dicionario["Seguro"] += 1
        elif 4 <= nivel <= 5:
            dicionario["Quase seguro"] += 1
        else:
            dicionario["Inseguro"] += 1
    return f"Muito seguro: {dicionario['Muito Seguro']}",f"Seguro: {dicionario['Seguro']}",f"Quase seguro: {dicionario['Quase seguro']}",f"Inseguro: {dicionario['Inseguro']}",

def questao_10_v1_nomes_com_r(lista):
    lista_r = []
    for nome in lista:
        if nome[0] == "R":
            lista_r.append(nome)
    return lista_r

def questao_10_v2_nomes_com_r(lista):
    return [nome for nome in lista if nome.startswith("R")]

def questao_11_v2_verifica_validade(lista, mes):
    return [produto for produto in lista if produto >= mes]

def questao_12_v2_saldo_positivo(lista_nomes,lista_saldo):
    return [lista_nomes[i] for i in range(len(lista_nomes)) if lista_saldo[i] >= 0]

def questao_13_v2_validade(lista_nomes, lista_validade, validade):
    return [f"{lista_nomes[i]}: {lista_validade[i]}" for i in range(len(lista_nomes)) if lista_validade[i] >= validade]

def questao_14_v2_faixa_etaria(lista_nomes, lista_idades, faixa_etaria):
    return [ lista_nomes[i] for i in range(len(lista_nomes)) if faixa_etaria[0] <= lista_idades[i] <= faixa_etaria[1]]

def questao_15_qtd_numero_par(lista):
    lista_par = set([numeros for numeros in lista if numeros % 2 == 0])
    return  lista_par, len(lista_par)