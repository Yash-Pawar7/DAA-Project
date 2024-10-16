import itertools
import random
from deap import base, creator, tools, algorithms

# Example Graph (Symmetric matrix)
graph = [[0, 10, 15, 20],
         [10, 0, 35, 25],
         [15, 35, 0, 30],
         [20, 25, 30, 0]]

n = len(graph)
start = 0

# 1. Brute Force
def tsp_brute_force(graph, start):
    vertices = list(range(len(graph)))
    vertices.remove(start)
    min_path = float('inf')
    for perm in itertools.permutations(vertices):
        current_path = sum(graph[perm[i]][perm[i+1]] for i in range(len(perm)-1))
        current_path += graph[start][perm[0]] + graph[perm[-1]][start]
        min_path = min(min_path, current_path)
    return min_path

# 2. Held-Karp Dynamic Programming
def tsp_held_karp(graph):
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0
    for mask in range(1 << n):
        for u in range(n):
            if mask & (1 << u):
                for v in range(n):
                    if not mask & (1 << v):
                        dp[mask | (1 << v)][v] = min(dp[mask | (1 << v)][v], dp[mask][u] + graph[u][v])
    return min(dp[(1 << n) - 1][i] + graph[i][0] for i in range(1, n))

# 3. Nearest Neighbor Heuristic
def tsp_nearest_neighbor(graph, start):
    visited = [False] * n
    visited[start] = True
    path_length = 0
    current_city = start
    for _ in range(n - 1):
        nearest_city = min([i for i in range(n) if not visited[i]], key=lambda x: graph[current_city][x])
        path_length += graph[current_city][nearest_city]
        visited[nearest_city] = True
        current_city = nearest_city
    return path_length + graph[current_city][start]

# 4. Genetic Algorithm TSP
def tsp_genetic_algorithm(graph, pop_size=50, cx_prob=0.7, mut_prob=0.2, generations=50):
    creator.create("FitnessMin", base.Fitness, weights=(-1,))
    creator.create("Individual", list, fitness=creator.FitnessMin)

    def eval_individual(individual):
        return sum(graph[individual[i]][individual[i + 1]] for i in range(len(individual) - 1)) + graph[individual[-1]][individual[0]],

    toolbox = base.Toolbox()
    toolbox.register("indices", random.sample, range(n), n)
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("mate", tools.cxOrdered)
    toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("evaluate", eval_individual)

    pop = toolbox.population(n=pop_size)
    algorithms.eaSimple(pop, toolbox, cxpb=cx_prob, mutpb=mut_prob, ngen=generations, verbose=False)
    best_ind = tools.selBest(pop, 1)[0]
    return eval_individual(best_ind)[0]

# Running all 4 methods
print("Brute Force:", tsp_brute_force(graph, start))
print("Held-Karp:", tsp_held_karp(graph))
print("Nearest Neighbor:", tsp_nearest_neighbor(graph, start))
print("Genetic Algorithm:", tsp_genetic_algorithm(graph))
