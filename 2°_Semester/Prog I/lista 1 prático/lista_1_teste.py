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