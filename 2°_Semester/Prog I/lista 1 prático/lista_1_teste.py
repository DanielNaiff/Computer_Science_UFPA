import lista_1_funções as f
lista1_mesmo_tamanho_string = ['abc', 'def', 'ghj']
lista2_mesmo_tamanho_string = ['gfd', 'rty', 'tre']
print('\033[0;31m-=\033[m'*30)
print('-=-=-Questao 1 Sem list comprehension-=-=-')
print(f.questao1_v1_concatenar_strings(lista1_mesmo_tamanho_string,lista2_mesmo_tamanho_string))
print()
print('-=-=-Questao 1 Com list comprehension-=-=-')
print(f.questao1_v2_concatenar_strings(lista1_mesmo_tamanho_string,lista2_mesmo_tamanho_string))
print()
print('\033[0;31m-=\033[m'*30)

lista_inteiros = [2, 56, 32, 7 , 89 , 4]
#print('-=-=-Questao 2 Com list comprehension-=-=-')
#print(f.calcular_proximo_primo(lista_inteiros))
#print()
#print('-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

lista_desordenada = ['dfhgdhjfgdhgfdhdfhbsd\gfrehtehyrthdg', 'jhjfgh', 'dfhfgh', 'fsdghfh']
print('-=-=-Questao 3 Sem list comprehension-=-=-')
print(f.questao_3_v1_menor_10(lista_desordenada))
print()
print('-=-=-Questao 3 Com list comprehension-=-=-')
print(f.questao_3_v2_menor_10(lista_desordenada))
print()
print('\033[0;31m-=\033[m'*30)

lista_heterogenea = ["dmsnfsdmf", [1,2,3,4,5]]
print('-=-=-Questao 4 Sem list comprehension-=-=-')
print(f.questao_4_lista_homogenea(lista_heterogenea))
print()
print('-=-=-Questao 4 Com list comprehension-=-=-')
print(f.questao_4_lista_homogenea(lista_heterogenea))
print()
print('\033[0;31m-=\033[m'*30)

lista_de_inteiros = [1,2,3]
lista_de_string = ["s","sd","sdfgfd"]
print('-=-=-Questao 5 Sem list comprehension-=-=-')
print(f.questao_5_v1_lista_de_string_com_correspondecia_a_uma_lista_de_inteiros(lista_de_string, lista_de_inteiros))
print()
print('-=-=-Questao 5 Com list comprehension-=-=-')
print(f.questao_5_v2_lista_de_string_com_correspondecia_a_uma_lista_de_inteiros(lista_de_string, lista_de_inteiros))
print()
print('\033[0;31m-=\033[m'*30)

lista_inteiros_1= [1,2,3]
lista_inteiros_2= [3,2,3]
lista_inteiros_3= [3,2,5]
print('-=-=-Questao 7 Sem list comprehension-=-=-')
print(f.questao_7_v1_reducao_para_encontrar_a_menor_soma_resultante(lista_inteiros_1,lista_inteiros_2,lista_inteiros_3))
print()
print('-=-=-Questao 7 Com list comprehension-=-=-')
print(f.questao_7_v2_reducao_para_encontrar_a_menor_soma_resultante(lista_inteiros_1,lista_inteiros_2,lista_inteiros_3))
print()
print('\033[0;31m-=\033[m'*30)

lista = ["abc", "defg", "hij", "klmno", "pqr"]
print('-=-=-Questao 8 Sem list comprehension-=-=-')
print(f.questao_8_v1_encontrar_maior_string(lista))
print()
print('-=-=-Questao 8 Com list comprehension-=-=-')
print(f.questao_8_v2_encontrar_maior_string(lista))
print()
print('\033[0;31m-=\033[m'*30)

lista = [3, 1, 4, 1, 5, 9, 2, 6]
print('-=-=-Questao 9 Sem list comprehension-=-=-')
print(f.questao_9_v1_somar_numeros_de_uma_lista(lista))
print()
print('-=-=-Questao 9 Com list comprehension-=-=-')
print(f.questao_9_v2_somar_numeros_de_uma_lista(lista))
print()
print('\033[0;31m-=\033[m'*30)

lista_strings = ["Daniel Naiff","Texto","Abc"]
print('-=-=-Questao 10 Sem list comprehension-=-=-')
print(f.questao_10_v1_concatena_de_string(lista_strings))
print()
print('-=-=-Questao 10 Com list comprehension-=-=-')
print(f.questao_10_v2_concatena_de_string(lista_strings))
print()
print('\033[0;31m-=\033[m'*30)

lista_inteiros = [4, 7, 11, 15, 20, 23, 29]
print('-=-=-Questao 11 Sem list comprehension-=-=-')
print(f.questao_11_v1_retorna_indice_maior_primo(lista_inteiros))
print()
print('-=-=-Questao 11 Com list comprehension-=-=-')
print(f.questao_11_v1_retorna_indice_maior_primo(lista_inteiros))
print()
print('\033[0;31m-=\033[m'*30)

lista_reais = [3,7,6,5,4]
print('-=-=-Questao 12 Sem list comprehension-=-=-')
print(f.questao_12_v1_desvio_padrao(lista_reais))
print()
print('-=-=-Questao 12 Com list comprehension-=-=-')
print(f.questao_12_v1_desvio_padrao(lista_reais))
print()
print('\033[0;31m-=\033[m'*30)

lista_inteiros = [38, 56, 2, 5, 16, 23, 72, 8, 12, 45]
numero_procurado = 23
print('-=-=-Questao 13 Sem list comprehension-=-=-')
print(f.questao_13_v1_busca_linear_desordenada(lista_inteiros, numero_procurado))
print()
print('-=-=-Questao 13 Com list comprehension-=-=-')
print(f.questao_13_v1_busca_linear_desordenada(lista_inteiros, numero_procurado))
print()
print('\033[0;31m-=\033[m'*30)

lista_inteiros = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72]
numero_procurado = 23
print('-=-=-Questao 14 Sem list comprehension-=-=-')
print(f.questao_14_v1_busca_linear_ordenada(lista_inteiros, numero_procurado))
print()
print('-=-=-Questao 14 Com list comprehension-=-=-')
print(f.questao_14_v1_busca_linear_ordenada(lista_inteiros, numero_procurado))
print()
print('\033[0;31m-=\033[m'*30)

lista_inteiros = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72]
numero_procurado = 23
print('-=-=-Questao 15 Sem list comprehension-=-=-')
print(f.questao_15_v1_buscar_binaria_inteiros(lista_inteiros, numero_procurado))
print()
print('-=-=-Questao 15 Com list comprehension-=-=-')
print(f.questao_15_v1_buscar_binaria_inteiros(lista_inteiros, numero_procurado))
print()
print('\033[0;31m-=\033[m'*30)

import random
lista = [random.randint(1, 100) for _ in range(1000)]
alvo = 23
print('-=-=-Questao 16 Sem list comprehension-=-=-')
print(f.questao_16_v1_buscar_binaria_inteiros(lista, alvo))
print()
print('-=-=-Questao 16 Funcao Count-=-=-')
print(f.questao_16_v2_buscar_binaria_inteiros(lista, alvo))
print()
print('\033[0;31m-=\033[m'*30)

lista = [random.randint(1, 20) for _ in range(1000)]
print('-=-=-Questao 17 Funcao Count-=-=-')
print(f.questao_17_v1_dicionario(lista))
print()
print('-=-=-Questao 17 Sem Funcao Count-=-=-')
print(f.questao_17_v2_dicionario(lista))
print()
print('\033[0;31m-=\033[m'*30)