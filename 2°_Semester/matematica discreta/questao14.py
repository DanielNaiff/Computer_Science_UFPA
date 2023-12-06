import time
import matplotlib.pyplot as plt
import random

def busca_binaria_iterativa(lista, elemento):
  inicio = 0
  fim = len(lista) - 1

  while inicio <= fim:
    meio = (inicio + fim) // 2

    if lista[meio] == elemento:
      return meio
    elif lista[meio] < elemento:
      inicio = meio + 1
    else:
      fim = meio - 1

  return -1

def medir_tempo_busca_binaria_iterativa(tamanho_lista):
  lista = sorted(random.sample(range(1, 1000000),tamanho_lista))  
  elemento = random.randint(1, 1000000)  
  inicio_tempo = time.time()
  busca_binaria_iterativa(lista, elemento)
  fim_tempo = time.time()
  return fim_tempo - inicio_tempo

def busca_binaria_recursiva(lista, elemento, inicio, fim):
  if inicio > fim:
    return -1

  meio = (inicio + fim) // 2

  if lista[meio] == elemento:
    return meio
  elif lista[meio] < elemento:
    return busca_binaria_recursiva(lista, elemento, meio + 1, fim)
  else:
    return busca_binaria_recursiva(lista, elemento, inicio, meio - 1)

def medir_tempo_busca_binaria_recursiva(tamanho_lista):
  lista = sorted(random.sample(range(1, 1000000),
                               tamanho_lista)) 
  elemento = random.randint(1, 1000000) 
  inicio = 0
  fim = len(lista) - 1
  inicio_tempo = time.time()
  busca_binaria_recursiva(lista, elemento, inicio, fim)
  fim_tempo = time.time()
  return fim_tempo - inicio_tempo

# colocando entradas para o gráfico
tamanhos = [100, 500, 1000, 5000, 10000, 20000, 40000, 80000, 160000,
            320000] 
tempos_iterativa = [
    medir_tempo_busca_binaria_iterativa(tamanho) for tamanho in tamanhos
]
tempos_recursiva = [
    medir_tempo_busca_binaria_recursiva(tamanho) for tamanho in tamanhos
]

# Plotando o gráfico 
plt.figure(figsize=(8, 5))
plt.plot(tamanhos,
         tempos_iterativa,
         marker='o',
         linestyle='-',
         color='b',
         label='Iterativa')
plt.plot(tamanhos,
         tempos_recursiva,
         marker='o',
         linestyle='-',
         color='r',
         label='Recursiva')
plt.title('Comparação de Desempenho: Busca Binária Iterativa vs Recursiva')
plt.xlabel('Tamanho da Lista')
plt.ylabel('Tempo de Execução (segundos)')
plt.legend()
plt.grid(True)
plt.show()