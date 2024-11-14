import random
import math

NUM_OPERADORES = 152  # Número de operadores

# Função Objetivo
def calcula_tempo_total(operadores, demanda, tempo_rodada, capacidade, atracoes):
    total_espera = 0
    for a in atracoes:
        tempo_espera = (demanda[a] * tempo_rodada[a]) / (capacidade[a] * operadores[a])
        total_espera += tempo_espera
    return total_espera

# Simulated Annealing
def simulated_annealing(demanda, tempo_rodada, capacidade, atracoes):
    temperature = 1000
    cooling_rate = 0.995
    iterations = 1000
    
    def construir_solucao():
        # Passo 1: Distribuir operadores proporcionalmente entre as atrações
        total_operadores = NUM_OPERADORES
        solution = {}
        total_atracoes = len(atracoes)
        
        for a in atracoes:
            solution[a] = round((1 / total_atracoes) * total_operadores)
        
        # Passo 2: Ajustar os operadores para garantir que a soma seja NUM_OPERADORES
        diff = total_operadores - sum(solution.values())
        if diff != 0:
            keys = list(solution.keys())
            random.shuffle(keys)
            for i in range(abs(diff)):
                solution[keys[i % len(keys)]] += 1 if diff > 0 else -1
        return solution

    # Cria a solução inicial com a soma de NUM_OPERADORES
    current_solution = construir_solucao()
    current_value = calcula_tempo_total(current_solution, demanda, tempo_rodada, capacidade, atracoes)
    
    best_solution = current_solution
    best_value = current_value
    
    for _ in range(iterations):
        neighbor = current_solution.copy()
        a = random.choice(atracoes)
        neighbor[a] = max(1, neighbor[a] + random.choice([-1, 1]))
        
        # Passo 1: Distribuir operadores proporcionalmente entre as atrações
        total_operadores = NUM_OPERADORES
        for a in atracoes:
            neighbor[a] = round((1 / len(atracoes)) * total_operadores)  # Distribui proporcionalmente
        
        # Passo 2: Ajustar os operadores para garantir que a soma seja NUM_OPERADORES
        diff = total_operadores - sum(neighbor.values())
        if diff != 0:
            keys = list(neighbor.keys())
            random.shuffle(keys)
            for i in range(abs(diff)):
                neighbor[keys[i % len(keys)]] += 1 if diff > 0 else -1
        
        neighbor_value = calcula_tempo_total(neighbor, demanda, tempo_rodada, capacidade, atracoes)
        
        if neighbor_value < current_value or random.random() < math.exp((current_value - neighbor_value) / temperature):
            current_solution = neighbor
            current_value = neighbor_value
        
        if current_value < best_value:
            best_solution = current_solution
            best_value = current_value
        
        temperature *= cooling_rate
    
    return best_solution, best_value
