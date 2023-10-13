import lista_1_funções as f
lista1_mesmo_tamanho_string = ['abc', 'def', 'ghj']
lista2_mesmo_tamanho_string = ['gfd', 'rty', 'tre']
print('-=-=-Questao 1 Sem list comprehension-=-=-')
print(f.questao1_v1_concatenar_strings(lista1_mesmo_tamanho_string,lista2_mesmo_tamanho_string))
print()
print('-=-=-Questao 1 Com list comprehension-=-=-')
print(f.questao1_v2_concatenar_strings(lista1_mesmo_tamanho_string,lista2_mesmo_tamanho_string))
print()
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

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
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

lista_heterogenea = ["dmsnfsdmf", [1,2,3,4,5]]
print('-=-=-Questao 4 Sem list comprehension-=-=-')
print(f.questao_4_lista_homogenea(lista_heterogenea))
print()
print('-=-=-Questao 4 Com list comprehension-=-=-')
print(f.questao_4_lista_homogenea(lista_heterogenea))
print()
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

lista_de_inteiros = [1,2,3]
lista_de_string = ["s","sd","sdfgfd"]
print('-=-=-Questao 5 Sem list comprehension-=-=-')
print(f.questao_5_v1_lista_de_string_com_correspondecia_a_uma_lista_de_inteiros(lista_de_string, lista_de_inteiros))
print()
print('-=-=-Questao 5 Com list comprehension-=-=-')
print(f.questao_5_v2_lista_de_string_com_correspondecia_a_uma_lista_de_inteiros(lista_de_string, lista_de_inteiros))
print()
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

lista_inteiros_1= [1,2,3]
lista_inteiros_2= [3,2,3]
lista_inteiros_3= [3,2,5]
print('-=-=-Questao 5 Sem list comprehension-=-=-')
print(f.questao_7_v1_reducao_para_encontrar_a_menor_soma_resultante(lista_inteiros_1,lista_inteiros_2,lista_inteiros_3))
print()
print('-=-=-Questao 5 Com list comprehension-=-=-')
print(f.questao_7_v2_reducao_para_encontrar_a_menor_soma_resultante(lista_inteiros_1,lista_inteiros_2,lista_inteiros_3))
print()
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')