import random

NUM_OPERADORES = 0  # Número de operadores

# Função Objetivo
def calcula_tempo_total(operadores, demanda, tempo_rodada, capacidade, atracoes):
    total_espera = 0
    for a in atracoes:
        tempo_espera = (demanda[a] * tempo_rodada[a]) / (capacidade[a] * max(operadores[a], 1))
        total_espera += tempo_espera
    return total_espera

# Algoritmo de Colônia de Formigas
def algoritmo_colonia_formigas(demanda, tempo_rodada, capacidade, atracoes, num_operadores):
    NUM_OPERADORES = num_operadores

    num_ants = 20
    num_iterations = 100
    evaporation_rate = 0.5
    alpha = 1
    beta = 2
    
    feromone = {a: 1 for a in atracoes}
    
    def calcular_probabilidade(feromone):
        total_prob = sum((feromone[a] ** alpha) for a in atracoes)
        probabilities = {a: (feromone[a] ** alpha) / total_prob for a in atracoes}
        return probabilities
    
    def construir_solucao():
        solution = {a: 0 for a in atracoes}
        total_operadores = NUM_OPERADORES
        
        probabilities = calcular_probabilidade(feromone)
        for _ in range(total_operadores):
            escolha = random.choices(atracoes, weights=[probabilities[a] for a in atracoes], k=1)[0]
            solution[escolha] += 1
        
        return solution
    
    best_solution = None
    best_value = float("inf")
    
    for _ in range(num_iterations):
        all_solutions = []
        all_values = []
        
        for _ in range(num_ants):
            solution = construir_solucao()
            value = calcula_tempo_total(solution, demanda, tempo_rodada, capacidade, atracoes)
            all_solutions.append(solution)
            all_values.append(value)
        
        # Atualizando os feromônios
        for a in atracoes:
            feromone[a] *= (1 - evaporation_rate)
        for i in range(num_ants):
            for a in atracoes:
                feromone[a] += (1 / all_values[i]) ** beta if a in all_solutions[i] else 0
        
        # Melhor solução da iteração
        iteration_best_index = all_values.index(min(all_values))
        iteration_best_solution = all_solutions[iteration_best_index]
        iteration_best_value = all_values[iteration_best_index]
        
        if iteration_best_value < best_value:
            best_solution = iteration_best_solution
            best_value = iteration_best_value
    
    return best_solution, best_value
