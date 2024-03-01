import numpy as np

class GeneticAlgorithm:
    def __init__(self, population_size, chromosome_length, gene_limits, mutation_rate=0.01, elitism_rate=0.1):
        self.population_size = population_size
        self.chromosome_length = chromosome_length
        self.gene_limits = gene_limits
        self.mutation_rate = mutation_rate
        self.elitism_rate = elitism_rate

    def _create_individual(self):
        return [np.random.randint(low=limit[0], high=limit[1] + 1) for limit in self.gene_limits]

    def _create_population(self):
        return [self._create_individual() for _ in range(self.population_size)]

    def _fitness(self, individual, evaluate_fn):
        return evaluate_fn(individual)

    def _mutate(self, individual):
        for i in range(len(individual)):
            if np.random.rand() < self.mutation_rate:
                individual[i] = np.random.randint(low=self.gene_limits[i][0], high=self.gene_limits[i][1] + 1)
        return individual

    def _crossover(self, parent1, parent2):
        crossover_point = np.random.randint(low=1, high=self.chromosome_length)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2

    def _select_parents(self, population, evaluate_fn):
        fitness_values = [self._fitness(individual, evaluate_fn) for individual in population]
        sorted_indices = np.argsort(fitness_values)
        selected_indices = sorted_indices[-2:]
        return [population[i] for i in selected_indices]

    def _next_generation(self, population, evaluate_fn):
        next_generation = []
        num_elites = int(self.elitism_rate * self.population_size)
        elites = sorted(population, key=lambda x: self._fitness(x, evaluate_fn))[-num_elites:]

        for _ in range(self.population_size - num_elites):
            parent1, parent2 = self._select_parents(population, evaluate_fn)
            child1, child2 = self._crossover(parent1, parent2)
            child1 = self._mutate(child1)
            child2 = self._mutate(child2)
            next_generation.extend([child1, child2])

        next_generation.extend(elites)
        return next_generation

    def run(self, evaluate_fn, max_generations=100):
        population = self._create_population()
        best_individual = None
        best_fitness = float('inf')

        for _ in range(max_generations):
            population = self._next_generation(population, evaluate_fn)
            fitness_values = [self._fitness(individual, evaluate_fn) for individual in population]
            min_fitness = min(fitness_values)
            if min_fitness < best_fitness:
                best_fitness = min_fitness
                best_individual = population[np.argmin(fitness_values)]

        return best_individual
