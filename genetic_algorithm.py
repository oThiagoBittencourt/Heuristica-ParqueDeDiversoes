import random

NUM_OPERADORES = 0  # Número de operadores

# Função Objetivo
def calcula_tempo_total(operadores, demanda, tempo_rodada, capacidade, atracoes):
    total_espera = 0
    for a in atracoes:
        tempo_espera = (demanda[a] * tempo_rodada[a]) / (capacidade[a] * operadores[a])
        total_espera += tempo_espera
    return total_espera

# Algoritmo Genético
def algoritmo_genetico(demanda, tempo_rodada, capacidade, atracoes, num_operadores):
    NUM_OPERADORES = num_operadores
    
    population_size = 50
    generations = 100
    mutation_rate = 0.1
    
    def construir_individuo():
        total_operadores = NUM_OPERADORES
        individuos = {}
        
        # Passo 1: Distribuir operadores proporcionalmente entre as atrações
        total_atracoes = len(atracoes)
        for a in atracoes:
            individuos[a] = round((1 / total_atracoes) * total_operadores)
        
        # Passo 2: Ajustar os operadores para garantir que a soma seja NUM_OPERADORES
        diff = total_operadores - sum(individuos.values())
        if diff != 0:
            keys = list(individuos.keys())
            random.shuffle(keys)
            for i in range(abs(diff)):
                individuos[keys[i % len(keys)]] += 1 if diff > 0 else -1
        
        return individuos
    
    population = [construir_individuo() for _ in range(population_size)]
    
    def avaliar(individuo):
        return calcula_tempo_total(individuo, demanda, tempo_rodada, capacidade, atracoes)
    
    def crossover(parent1, parent2):
        child = {}
        for a in atracoes:
            child[a] = parent1[a] if random.random() > 0.5 else parent2[a]
        
        # Passo 3: Garantir que a soma dos operadores seja NUM_OPERADORES após crossover
        total_operadores = NUM_OPERADORES
        diff = total_operadores - sum(child.values())
        if diff != 0:
            keys = list(child.keys())
            random.shuffle(keys)
            for i in range(abs(diff)):
                child[keys[i % len(keys)]] += 1 if diff > 0 else -1
        
        return child
    
    def mutacao(individuo):
        mutated = individuo.copy()
        a = random.choice(atracoes)
        mutated[a] = max(1, mutated[a] + random.choice([-1, 1]))
        
        # Passo 4: Garantir que a soma dos operadores seja NUM_OPERADORES após mutação
        total_operadores = NUM_OPERADORES
        diff = total_operadores - sum(mutated.values())
        if diff != 0:
            keys = list(mutated.keys())
            random.shuffle(keys)
            for i in range(abs(diff)):
                mutated[keys[i % len(keys)]] += 1 if diff > 0 else -1
        
        return mutated
    
    for gen in range(generations):
        population.sort(key=avaliar)
        next_population = population[:10]  # Seleciona os 10 melhores
        while len(next_population) < population_size:
            parent1, parent2 = random.sample(population[:20], 2)
            child = crossover(parent1, parent2)
            if random.random() < mutation_rate:
                child = mutacao(child)
            next_population.append(child)
        
        population = next_population
    
    best_solution = population[0]
    best_value = avaliar(best_solution)
    return best_solution, best_value
