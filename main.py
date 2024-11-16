from genetic_algorithm import algoritmo_genetico
from simulated_annealing import simulated_annealing
from ant_colony_optimization import algoritmo_colonia_formigas

# Definindo os parâmetros do problema
atracoes = ['Montanha Russa', 'Carrossel', 'Casa Assombrada', 'Roda-Gigante', 'Bate-Bate']
demanda = {'Montanha Russa': 400, 'Carrossel': 70, 'Casa Assombrada': 110, 'Roda-Gigante': 260, 'Bate-Bate': 150}
tempo_rodada = {'Montanha Russa': 3, 'Carrossel': 10, 'Casa Assombrada': 15, 'Roda-Gigante': 10, 'Bate-Bate': 5}
capacidade = {'Montanha Russa': 30, 'Carrossel': 10, 'Casa Assombrada': 10, 'Roda-Gigante': 30, 'Bate-Bate': 15}

num_operadores = 52

# Executando os algoritmos
def executar_algoritmos():
    print("Executando Algoritmo Genético (GA)...")
    solucao_ga, tempo_ga = algoritmo_genetico(demanda, tempo_rodada, capacidade, atracoes, num_operadores)
    print(f"GA - Melhor Solução: {solucao_ga} com tempo de espera: {tempo_ga}")
    
    print("\nExecutando Simulated Annealing (SA)...")
    solucao_sa, tempo_sa = simulated_annealing(demanda, tempo_rodada, capacidade, atracoes, num_operadores)
    print(f"SA - Melhor Solução: {solucao_sa} com tempo de espera: {tempo_sa}")
    
    print("\nExecutando Algoritmo de Colônia de Formigas (ACO)...")
    solucao_aco, tempo_aco = algoritmo_colonia_formigas(demanda, tempo_rodada, capacidade, atracoes, num_operadores)
    print(f"ACO - Melhor Solução: {solucao_aco} com tempo de espera: {tempo_aco}")
    
    # Comparação entre os resultados
    resultados = {
        'GA': (solucao_ga, tempo_ga),
        'SA': (solucao_sa, tempo_sa),
        'ACO': (solucao_aco, tempo_aco)
    }
    
    melhor_algoritmo = min(resultados, key=lambda k: resultados[k][1])
    print(f"\nMelhor Algoritmo: {melhor_algoritmo} com tempo de espera: {resultados[melhor_algoritmo][1]}")

# Executar os algoritmos
executar_algoritmos()
