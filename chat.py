class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.distancias = [[0]*len(vertices) for _ in range(len(vertices))]

    def adicionar_aresta(self, u, v, distancia):
        self.distancias[u][v] = distancia
        self.distancias[v][u] = distancia

    def calcular_distancia(self, rota):
        distancia_total = 0
        for i in range(len(rota) - 1):
            distancia_total += self.distancias[rota[i]][rota[i+1]]
        distancia_total += self.distancias[rota[-1]][rota[0]]
        return distancia_total

    def permutacoes(self, rota_atual, vertices_disponiveis):
        if not vertices_disponiveis:
            distancia = self.calcular_distancia(rota_atual)
            return rota_atual, distancia

        melhor_rota = None
        melhor_distancia = float('inf')

        for i in range(len(vertices_disponiveis)):
            vertice = vertices_disponiveis[i]
            novo_rota = rota_atual + [vertice]
            novos_vertices = vertices_disponiveis[:i] + vertices_disponiveis[i+1:]
            rota, distancia = self.permutacoes(novo_rota, novos_vertices)

            if distancia < melhor_distancia:
                melhor_distancia = distancia
                melhor_rota = rota

        return melhor_rota, melhor_distancia

    def caixeiro_viajante(self):
        return self.permutacoes([0], list(range(1, len(self.vertices))))

# Exemplo de uso:
cidades = ['A', 'B', 'C', 'D']
grafo = Grafo(cidades)
grafo.adicionar_aresta(0, 3, 20)
grafo.adicionar_aresta(1, 2, 35)
grafo.adicionar_aresta(1, 3, 25)
grafo.adicionar_aresta(2, 3, 30)

melhor_rota, melhor_distancia = grafo.caixeiro_viajante()
print(f"Melhor rota: {[cidades[i] for i in melhor_rota]}")
print(f"Distância total: {melhor_distancia}")
