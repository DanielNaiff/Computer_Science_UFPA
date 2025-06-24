import random
import time
import statistics

bestStates = []

def countConflicts(array):
    linhas = {}
    diag1 = {}
    diag2 = {}
    conflicts = 0

    for col, row in enumerate(array):
        linhas[row] = linhas.get(row, 0) + 1
        diag1[row - col] = diag1.get(row - col, 0) + 1
        diag2[row + col] = diag2.get(row + col, 0) + 1

    for d in (linhas, diag1, diag2):
        for count in d.values():
            if count > 1:
                conflicts += count * (count - 1) // 2

    return conflicts

def random_initial_state(n=8):
    return [random.randint(0, n - 1) for _ in range(n)]

def stochastic_hill_climbing(state):
    n = len(state)
    current_conflicts = countConflicts(state)
    interactions = 0

    while current_conflicts > 0:
        neighbors = []
        best_conflicts = current_conflicts

        for col in range(n):
            for row in range(n):
                if row != state[col]:
                    new_state = state.copy()
                    new_state[col] = row
                    conflicts = countConflicts(new_state)
                    if conflicts <= best_conflicts:
                        if conflicts < best_conflicts:
                            neighbors = [(new_state, conflicts)]
                            best_conflicts = conflicts
                        else:
                            neighbors.append((new_state, conflicts))

        if not neighbors:
            break

        state, current_conflicts = random.choice(neighbors)
        bestStates.append((state.copy(), current_conflicts))
        interactions += 1

    return state, interactions  

def showBestSolutions(solutions, top_n=5):
    unique_solutions = list({tuple(state): conflicts for state, conflicts in solutions}.items())
    unique_solutions.sort(key=lambda x: x[1])

    print(f"\nTop {top_n} melhores soluções encontradas:")
    for i, (state, conflicts) in enumerate(unique_solutions[:top_n]):
        print(f"{i+1}) {state} - Conflitos: {conflicts}")

if __name__ == "__main__":
    interaction_counts = []
    execution_times = []

    for _ in range(50):
        initial = random_initial_state()

        start_time = time.perf_counter()
        _, interactions = stochastic_hill_climbing(initial)
        end_time = time.perf_counter()

        interaction_counts.append(interactions)
        execution_times.append(end_time - start_time)

    # Estatísticas
    media_interacoes = statistics.mean(interaction_counts)
    desvio_interacoes = statistics.stdev(interaction_counts)

    media_tempo = statistics.mean(execution_times)
    desvio_tempo = statistics.stdev(execution_times)

    # Resultados
    print(f"\n--- Estatísticas após 50 execuções ---")
    print(f"Média de interações: {media_interacoes:.2f}")
    print(f"Desvio padrão das interações: {desvio_interacoes:.2f}")
    print(f"Média de tempo de execução: {media_tempo:.6f} segundos")
    print(f"Desvio padrão do tempo: {desvio_tempo:.6f} segundos")

    # Mostrar top 5 soluções
    showBestSolutions(bestStates)
