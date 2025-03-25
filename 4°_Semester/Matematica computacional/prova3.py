import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation
from itertools import combinations

class ACO_TSP:
    def __init__(self, cities, n_ants=10, n_iterations=100, alpha=1, beta=2, rho=0.5, q=100):
        """
        Inicializa o algoritmo ACO para o TSP.
        
        Parâmetros:
        - cities: lista de coordenadas das cidades (numpy array)
        - n_ants: número de formigas
        - n_iterations: número de iterações
        - alpha: peso do feromônio na escolha do caminho
        - beta: peso da heurística (distância inversa) na escolha do caminho
        - rho: taxa de evaporação do feromônio
        - q: constante para cálculo do depósito de feromônio
        """
        self.cities = cities
        self.n_cities = len(cities)
        self.n_ants = n_ants
        self.n_iterations = n_iterations
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.q = q
        
        # Calcula matriz de distâncias
        self.distances = self._calculate_distances()
        
        # Inicializa matriz de feromônios com valores pequenos
        self.pheromone = np.ones((self.n_cities, self.n_cities)) * 0.1
        
        # Armazena histórico de fitness
        self.best_fitness_history = []
        self.worst_fitness_history = []
        self.best_path_history = []
        
    def _calculate_distances(self):
        """Calcula a matriz de distâncias entre todas as cidades."""
        distances = np.zeros((self.n_cities, self.n_cities))
        for i in range(self.n_cities):
            for j in range(self.n_cities):
                distances[i,j] = np.linalg.norm(self.cities[i] - self.cities[j])
        return distances
    
    def _calculate_path_distance(self, path):
        """Calcula a distância total de um caminho."""
        distance = 0
        for i in range(self.n_cities - 1):
            distance += self.distances[path[i], path[i+1]]
        distance += self.distances[path[-1], path[0]]  # Volta para a cidade inicial
        return distance
    
    def _select_next_city(self, current_city, unvisited, pheromone, distances):
        """Seleciona a próxima cidade baseada no feromônio e distância."""
        probabilities = []
        total = 0
        
        for city in unvisited:
            if distances[current_city, city] == 0:
                prob = 0
            else:
                prob = (pheromone[current_city, city] ** self.alpha) * \
                       ((1 / distances[current_city, city]) ** self.beta)
            probabilities.append(prob)
            total += prob
        
        if total == 0:
            # Se todas as probabilidades são zero, escolhe aleatoriamente
            return random.choice(unvisited)
        
        probabilities = [p/total for p in probabilities]
        return random.choices(unvisited, weights=probabilities, k=1)[0]
    
    def _construct_solutions(self):
        """Constrói soluções para todas as formigas."""
        all_paths = []
        all_distances = []
        
        for _ in range(self.n_ants):
            # Inicia em uma cidade aleatória
            start_city = random.randint(0, self.n_cities - 1)
            path = [start_city]
            unvisited = set(range(self.n_cities)) - {start_city}
            
            while unvisited:
                next_city = self._select_next_city(path[-1], list(unvisited), 
                                                  self.pheromone, self.distances)
                path.append(next_city)
                unvisited.remove(next_city)
            
            distance = self._calculate_path_distance(path)
            all_paths.append(path)
            all_distances.append(distance)
        
        return all_paths, all_distances
    
    def _update_pheromones(self, all_paths, all_distances):
        """Atualiza a matriz de feromônios com evaporação e depósito."""
        # Evaporação
        self.pheromone *= (1 - self.rho)
        
        # Depósito de feromônio
        for path, distance in zip(all_paths, all_distances):
            delta_pheromone = self.q / distance
            for i in range(self.n_cities - 1):
                self.pheromone[path[i], path[i+1]] += delta_pheromone
                self.pheromone[path[i+1], path[i]] += delta_pheromone  # Feromônio é simétrico
            # Volta para a cidade inicial
            self.pheromone[path[-1], path[0]] += delta_pheromone
            self.pheromone[path[0], path[-1]] += delta_pheromone
    
    def run(self):
        """Executa o algoritmo ACO."""
        best_path = None
        best_distance = float('inf')
        
        for iteration in range(self.n_iterations):
            # Constrói soluções
            all_paths, all_distances = self._construct_solutions()
            
            # Atualiza feromônios
            self._update_pheromones(all_paths, all_distances)
            
            # Encontra a melhor e pior solução desta iteração
            current_best_idx = np.argmin(all_distances)
            current_worst_idx = np.argmax(all_distances)
            current_best_distance = all_distances[current_best_idx]
            current_worst_distance = all_distances[current_worst_idx]
            
            # Atualiza a melhor solução global
            if current_best_distance < best_distance:
                best_distance = current_best_distance
                best_path = all_paths[current_best_idx]
            
            # Armazena histórico
            self.best_fitness_history.append(current_best_distance)
            self.worst_fitness_history.append(current_worst_distance)
            self.best_path_history.append(best_path.copy())
            
            print(f"Iteração {iteration + 1}: Melhor = {current_best_distance:.2f}, Pior = {current_worst_distance:.2f}")
        
        return best_path, best_distance
    
    def plot_results(self):
        """Plota os resultados: cidades, melhor rota e evolução do fitness."""
        plt.figure(figsize=(15, 5))
        
        # Gráfico 1: Cidades e melhor rota
        plt.subplot(1, 3, 1)
        plt.scatter(self.cities[:, 0], self.cities[:, 1], c='red')
        for i, city in enumerate(self.cities):
            plt.text(city[0], city[1], str(i))
        
        best_path = self.best_path_history[-1]
        best_path_cities = self.cities[best_path + [best_path[0]]]
        plt.plot(best_path_cities[:, 0], best_path_cities[:, 1], 'b-')
        plt.title("Melhor Rota Encontrada")
        plt.xlabel("Coordenada X")
        plt.ylabel("Coordenada Y")
        
        # Gráfico 2: Evolução do fitness (melhor e pior)
        plt.subplot(1, 3, 2)
        plt.plot(self.best_fitness_history, 'g-', label='Melhor Fitness')
        plt.plot(self.worst_fitness_history, 'r-', label='Pior Fitness')
        plt.title("Evolução do Fitness por Iteração")
        plt.xlabel("Iteração")
        plt.ylabel("Distância do Caminho")
        plt.legend()
        plt.grid(True)
        
        # Gráfico 3: Feromônios na última iteração
        plt.subplot(1, 3, 3)
        plt.imshow(self.pheromone, cmap='hot', interpolation='nearest')
        plt.title("Matriz de Feromônios Final")
        plt.xlabel("Cidade")
        plt.ylabel("Cidade")
        plt.colorbar()
        
        plt.tight_layout()
        plt.show()

# Exemplo de uso
if __name__ == "__main__":
    # Gera cidades aleatórias
    np.random.seed(42)
    n_cities = 15
    cities = np.random.rand(n_cities, 2) * 100
    
    # Cria e executa o ACO
    aco = ACO_TSP(cities, n_ants=10, n_iterations=50, alpha=1, beta=3, rho=0.3, q=100)
    best_path, best_distance = aco.run()
    
    # Plota resultados
    aco.plot_results()
    
    print(f"\nMelhor caminho encontrado: {best_path}")
    print(f"Distância total: {best_distance:.2f}")