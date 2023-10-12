import funcoes as f
lista = [1,2,3,4,5,6,7]
lista_reversa = f.criar_lista_reversa(lista)
print(lista_reversa)

lista_indice_impar=f.criar_lista_indice_impar(lista)
print(lista_indice_impar)

lista_primeira_metade=f.criar_lista_primeira_metade(lista)
print(lista_primeira_metade)

soma=f.somar_lista([1,54,6,4])
print(soma)

maior_valor=f.maior_valor_lista(lista)
print(maior_valor)

cadastros=[{'nome':'renato','e-mail':'renato@email.com','saldo':58},
          {'nome':'maria','e-mail':'maria@email.com','saldo':100.50},
          {'nome':'jose','e-mail':'jose@gmail.com','saldo':1025},
          {'nome':'joao','e-mail':'joao@gmail.com','saldo':122.76}]
print(cadastros[2]['e-mail'])


filtro_email=f.filtrar_por_email(cadastros,'provedor')
print(filtro_email)


saldo=f.calcular_saldo_medio(cadastros)
print(saldo)

filtr_saldo=f.filtrar_saldo(cadastros,100,'MENOR')

lista=[1,2,'A','B',3,'C']

lista_filtrada=f.filtrar_por_tipo(lista,str)
print(lista_filtrada)

lista_nomes=f.extrair_nomes(cadastros)
print(lista_nomes)


lista_tamanho_nomes=f.calcular_tamanho_nomes(lista_nomes)

lista = [2.14,3.12,2.5,3.1,7.88]

lista = f.transformar_real_inteiro(lista)
print(lista)