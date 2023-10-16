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

#################################################################################################

lista = [8,18,4,20,1,12]
print('\033[0;32m-=\033[m'*30)
print('-=-=-Questao 1 Sem list comprehension-=-=-')
print(f.questao_1_v1_embalagens_fora_do_padrao(lista))
print()
print('-=-=-Questao 1 Com list comprehension-=-=-')
print(f.questao_1_v2_embalagens_fora_do_padrao(lista))
print()
print('\033[0;32m-=\033[m'*30)

lista = [3.5, 6, 7.5, 8, 9, 9, 5, 10, 7.5, 8 ]
media = 7
print('-=-=-Questao 2 Sem list comprehensiont-=-=-')
print(f.questao_2_v1_media_aprovados(lista, media))
print()
print('-=-=-Questao 2 Com list comprehension-=-=-')
print(f.questao_2_v2_media_aprovados(lista, media))
print()
print('\033[0;32m-=\033[m'*30)

lista = [1.7, 1.88, 1.5, 1.32, 1.68, 1.59]
print('-=-=-Questao 3 Sem list comprehension-=-=-')
print(f.questao_3_v1_maior_altura(lista))
print()
print('\033[0;32m-=\033[m'*30)

lista = [3, 5, 4, 6, 3, 2, 8, 10 ]
print('-=-=-Questao 4 Sem list comprehension-=-=-')
print(f.questao_4_v1_media_numeros_pares(lista))
print()
print('\033[0;32m-=\033[m'*30)

lista = ["TACG", "GAGC", "ATUC", "TAGC", "GAGC"  ]
base_alvo = "GAGC"
print('-=-=-Questao 5 Sem list comprehension-=-=-')
print(f.questao_5_v1_frequencia_de_bases_nitrogenadas(lista, base_alvo))
print()
print('\033[0;32m-=\033[m'*30)

lista = [2, 3, 4, 7, 1, 2, 30, 13, 25, 1, 3]
velocidade = 20
print('-=-=-Questao 6 Sem list comprehension-=-=-')
print(f.questao_6_v1_sprint_backlog(lista,velocidade))
print()
print('\033[0;32m-=\033[m'*30)

lista = [3, 2, 5, 4, 8, 6, 7, 10, 12, 13, 11]
print('-=-=-Questao 7 Sem list comprehension-=-=-')
print(f.questao_7_v1_ordem_chegada(lista))
print()
print('\033[0;32m-=\033[m'*30)

lista = ["E", "E", "B", "B", "R", "E", "B", "R", "I", "I", "R", "R", "I"]
print('-=-=-Questao 8 Sem list comprehension-=-=-')
print(f.questao_8_v1_conta_conceito(lista))
print()
print('\033[0;32m-=\033[m'*30)

lista = [0, 0 ,1, 3, 2, 4, 5, 6, 1, 2, 7]
print('-=-=-Questao 9 Sem list comprehension-=-=-')
print(f.questao_9_v1_nivel_de_vunerabilidade(lista))
print()
print('\033[0;32m-=\033[m'*30)

lista = ["Ramon", "Arnaldo", "Raquel", "Pedro", "Rafael"]
print('-=-=-Questao 10 Sem list comprehension-=-=-')
print(f.questao_10_v1_nomes_com_r(lista))
print()
print('-=-=-Questao 10 Com list comprehension-=-=-')
print(f.questao_10_v2_nomes_com_r(lista))
print()
print('\033[0;32m-=\033[m'*30)

lista = [5, 4, 3, 11, 1, 1, 8 ,10, 11, 3, 4, 2, 10]
mes = 8
print('-=-=-Questao 11 Com list comprehension-=-=-')
print(f.questao_11_v2_verifica_validade(lista, mes))
print()
print('\033[0;32m-=\033[m'*30)

lista_nomes = ["Ramon", "Arnaldo", "Raquel", "Pedro", "Rafael"]
lista_saldo = [100, -500, -1, 1500, 90]
print('-=-=-Questao 12 Com list comprehension-=-=-')
print(f.questao_12_v2_saldo_positivo(lista_nomes,lista_saldo))
print()
print('\033[0;32m-=\033[m'*30)

lista_nomes = ["AA", "AB", "BA", "BB", "CA", "AC"]
lista_validade = [5, 4, 3, 11, 12, 1]
validade = 8
print('-=-=-Questao 13 Com list comprehension-=-=-')
print(f.questao_13_v2_validade(lista_nomes, lista_validade, validade))
print()
print('\033[0;32m-=\033[m'*30)

lista_nomes = ["Ramon", "Arnaldo", "Raquel", "Pedro", "Rafael"]
lista_idades = [23, 45, 27, 60, 45]
faixa_etaria = [20,30]
print('-=-=-Questao 14 Com list comprehension-=-=-')
print(f.questao_14_v2_faixa_etaria(lista_nomes, lista_idades, faixa_etaria))
print()
print('\033[0;32m-=\033[m'*30)

lista = [0, 0 ,1, 3, 2, 4, 5, 6, 1, 2, 7]
print('-=-=-Questao 15 Com list comprehension-=-=-')
print(f.questao_15_v2_qtd_numero_par(lista))
print()
print('\033[0;32m-=\033[m'*30)

lista_nomes = ["Amanda", "Amaral", "Arnaldo", "Bruno"]
palavra = "Ama"
print('-=-=-Questao 16 Com list comprehension-=-=-')
print(f.quetao_16_v2_buscar(lista_nomes, palavra))
print()
print('\033[0;32m-=\033[m'*30)

lista_inteiros = [2, 4, 6, 8, 11, 12, 14 ]
print('-=-=-Questao 17 Sem list comprehension-=-=-')
print(f.questao_17_v1_eh_pa(lista_inteiros))
print()
print('-=-=-Questao 17 Com list comprehension-=-=-')
print(f.questao_17_v2_eh_pa(lista_inteiros))
print()
print('\033[0;32m-=\033[m'*30)

lista_1 = [0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0]
lista_2 = [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0]
print('-=-=-Questao 18 Sem list comprehension-=-=-')
print(f.questao_18_v1_distancia_hamming(lista_1, lista_2))
print()
print('-=-=-Questao 18 Com list comprehension-=-=-')
print(f.questao_18_v2_distancia_hamming(lista_1, lista_2))
print()
print('\033[0;32m-=\033[m'*30)