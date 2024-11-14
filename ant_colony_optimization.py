import random

NUM_OPERADORES = 152  # Número de operadores

# Função Objetivo
def calcula_tempo_total(operadores, demanda, tempo_rodada, capacidade, atracoes):
    total_espera = 0
    for a in atracoes:
        tempo_espera = (demanda[a] * tempo_rodada[a]) / (capacidade[a] * operadores[a])
        total_espera += tempo_espera
    return total_espera

# Algoritmo de Colônia de Formigas
def algoritmo_colonia_formigas(demanda, tempo_rodada, capacidade, atracoes):
    num_ants = 20
    num_iterations = 100
    evaporation_rate = 0.5
    alpha = 1
    beta = 2
    
    feromone = {a: 1 for a in atracoes}
    
    def calcular_probabilidade(ant, feromone):
        total_prob = 0
        for a in atracoes:
            total_prob += feromone[a] ** alpha
        probabilities = {a: (feromone[a] ** alpha) / total_prob for a in atracoes}
        return probabilities
    
    def construir_solucao():
        solution = {}
        total_operadores = NUM_OPERADORES
        total_atracoes = len(atracoes)
        
        # Distribuindo operadores proporcionalmente
        for a in atracoes:
            solution[a] = round((1 / total_atracoes) * total_operadores)
        
        # Ajustando os operadores para garantir que a soma seja NUM_OPERADORES
        diff = total_operadores - sum(solution.values())
        if diff != 0:
            keys = list(solution.keys())
            random.shuffle(keys)
            for i in range(abs(diff)):
                solution[keys[i % len(keys)]] += 1 if diff > 0 else -1
        return solution
    
    for _ in range(num_iterations):
        all_solutions = []
        all_values = []
        
        for _ in range(num_ants):
            solution = construir_solucao()
            value = calcula_tempo_total(solution, demanda, tempo_rodada, capacidade, atracoes)
            all_solutions.append(solution)
            all_values.append(value)
        
        for i in range(num_ants):
            for a in atracoes:
                feromone[a] = (1 - evaporation_rate) * feromone[a] + (1 / all_values[i]) ** beta
        
        best_index = all_values.index(min(all_values))
        best_solution = all_solutions[best_index]
        best_value = all_values[best_index]
    
    return best_solution, best_value
