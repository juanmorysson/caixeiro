import itertools

def calculate_distance(path, graph, retorno):
    distance = 0
    for i in range(len(path) - 1):
        custo = graph[path[i]][path[i + 1]]
        if custo > 0:
            distance += graph[path[i]][path[i + 1]]
        else:
            distance += float('inf')
    distance += retorno[path[-1]]  # Retorna à cidade de origem
    return distance


def tsp_brute_force(graph, inicio, retorno=None):
    n = len(graph)
    cities = list(range(n))
    min_path = None
    min_distance = float('inf')
    print("Criando lista")
    lista_p = []
    for perm in itertools.permutations(cities):
        for p in itertools.combinations_with_replacement(perm, len(cities)):
            lista_p.append(p)
    print("limpa")
    lista = set(lista_p)
    print(len(lista))
    # Itera por todas as permutações possíveis das cidades
    for perm in lista:
        current_path = list(perm)
        if current_path[0] == inicio:
            complete = True
            for c in cities:
                if not current_path.__contains__(c):
                    complete = False
            if complete:
                current_distance = calculate_distance(current_path, graph, retorno)
                if current_distance < min_distance:
                    min_distance = current_distance
                    min_path = current_path

    return min_path, min_distance


# Exemplo de uso
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

#path, distance = tsp_brute_force(graph)
#print(f"Melhor caminho: {path}")
#print(f"Menor distância: {distance}")
