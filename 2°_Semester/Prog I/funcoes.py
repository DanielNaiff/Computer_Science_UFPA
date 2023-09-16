def criar_lista_reversa(lista):
    return lista[::-1]

#sub lista indices impares   
def criar_lista_indice_impar(lista):
    return lista [1::2]


#sub lista metade da lista
def criar_lista_primeira_metade(lista):
    meio = len(lista)//2
    return lista[:meio]

def somar_lista(lista):
    total=0
    for valor in lista:
        total=total+valor
    return total

#maior valor da lista
def maior_valor_lista(lista):
    maior=lista[0]
    for valor in lista[1:]:
        maior=(maior+valor+abs(maior-valor))//2
    return maior

def calcular_saldo_medio(cadastros):
    saldo_medio=0
    for elemento in cadastros:
        saldo_medio+=elemento['saldo']
    return saldo_medio/len(cadastros)

def filtrar_por_email(cadastros,provedor):
    lista_filtrada=[]
    for elemento in cadastros:
        if provedor not in elemento ['e-mail']:
            lista_filtrada.append(elemento)
    return lista_filtrada

def filtrar_saldo(cadastros,saldo,operador):
    lista_filtrada=[]
    for elemento in cadastros:
        if operador == 'MAIOR' and elemento['saldo'] > saldo  or operador =="MENOR" and elemento['saldo']<saldo:
            lista_filtrada.append(elemento)
    return lista_filtrada

def filtrar_por_tipo(lista,tipo):
    lista_filtrada=[]
    for item in lista:
        if type(item) == tipo:
            lista_filtrada.append(item)
    return lista_filtrada

def extrair_nomes(cadastros):
    lista_nomes=[]
    for item in cadastros:
        lista_nomes.append(item['nome'])
    return lista_nomes

def formatar_caixa_alta(lista,formatacao):
    lista_formatada=[]
    for item in lista:
        lista_formatada.append(item.upper())
    return lista_formatada


def formatar_caixa_baixa(lista,formatacao):
    lista_formatada=[]
    for item in lista:
        lista_formatada.append(item.lower())
    return lista_formatada 

def formatar_nomes(lista,formatacao):
    """
    mapeia uma lista de string para uma lista de string,considerando a opção de formatação passada como segundo argumento
    argumentos: lista de string
      lista: lista de string
      formatação: string (ex:CAIXA_ALTA,CAIXA_BAIXA)
    retorno: lista de string formatada ou uma mensagem de aviso
    """
    if formatacao == 'CAIXA_ALTA':
        return formatar_caixa_alta(lista)
    elif formatacao == 'CAIXA_BAIXA':
        return formatar_caixa_baixa(lista)
    else:
        return 'o segundo argumento é inválido'
    
def calcular_tamanho_nomes(lista):
    return [len(item) for item in lista]
    lista_tamanho_nomes=[]
    for item in lista:
        lista_tamanho_nomes.append(len(item))
    return lista_tamanho_nomes
# exercicios aula 14/09/2023
#mapeamento
def mapear_inteiro(item):
    import math as m
    x1 = str(item)
    idx = x1.index('.')
    x2 = x1[idx+1:]
    x3 = int(x2)
    # controle de fluxo de condição
    if x3 % 2 == 0:
        return m.floor(item)
    else:
        return m.ceil(item)

def transformar_real_inteiro(lista):
    return [mapear_inteiro(item) for item in lista]
    
#mapeamento
def mapear_3_em_1(lista_1,lista_2,lista_3):
    return [max(item) + min(item)\
        for item in zip(lista_1,lista_2,lista_3)
    ]
#filtro
def construir_lista_palindromo(lista):
    # ordem de execução parte2, parte 3 e parte 1
    return [x\
             for x,y in zip(lista,lista[::-1])\
                  if x == y]

def encontrar_maior_string(lista):
    #valor = lista[0]
    #idx = 0
    #tamanho = len(valor)
    dicionario = {
                    'valor': lista[0],
                    'indice': 0,
                    'tamanho': len(lista[0])
                }
    for item in lista[1:]:
        if len(item) > dicionario['tamanho']:
            dicionario["valor"] = item
            dicionario["indice"] = lista.index(item)
            dicionario["tamanho"] = len(item)
    return dicionario
