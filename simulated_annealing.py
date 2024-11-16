import random
import math

NUM_OPERADORES = 0  # Número de operadores

# Função Objetivo
def calcula_tempo_total(operadores, demanda, tempo_rodada, capacidade, atracoes):
    total_espera = 0
    for a in atracoes:
        tempo_espera = (demanda[a] * tempo_rodada[a]) / (capacidade[a] * max(operadores[a], 1))
        total_espera += tempo_espera
    return total_espera

# Simulated Annealing
def simulated_annealing(demanda, tempo_rodada, capacidade, atracoes, num_operadores):
    NUM_OPERADORES = num_operadores

    temperature = 1000
    cooling_rate = 0.995
    iterations = 1000

    def construir_solucao_inicial():
        total_operadores = NUM_OPERADORES
        solution = {a: 1 for a in atracoes}  # Garante que cada atração tenha pelo menos 1 operador
        restante = total_operadores - len(atracoes)
        for _ in range(restante):
            escolha = random.choice(atracoes)
            solution[escolha] += 1
        return solution

    def gerar_vizinho(solution):
        neighbor = solution.copy()
        # Seleciona duas atrações diferentes para redistribuir operadores
        a1, a2 = random.sample(atracoes, 2)
        if neighbor[a1] > 1:  # Garante que nenhuma atração fique com menos de 1 operador
            neighbor[a1] -= 1
            neighbor[a2] += 1
        return neighbor

    current_solution = construir_solucao_inicial()
    current_value = calcula_tempo_total(current_solution, demanda, tempo_rodada, capacidade, atracoes)

    best_solution = current_solution
    best_value = current_value

    for _ in range(iterations):
        neighbor = gerar_vizinho(current_solution)
        neighbor_value = calcula_tempo_total(neighbor, demanda, tempo_rodada, capacidade, atracoes)

        # Critério de aceitação de soluções
        if neighbor_value < current_value or random.random() < math.exp((current_value - neighbor_value) / temperature):
            current_solution = neighbor
            current_value = neighbor_value

        if current_value < best_value:
            best_solution = current_solution
            best_value = current_value

        # Reduz a temperatura
        temperature *= cooling_rate

    return best_solution, best_value
