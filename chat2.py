import pandas as pd

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.distancias = [[0] * len(vertices) for _ in range(len(vertices))]

    def adicionar_aresta(self, u, v, distancia):
        self.distancias[u][v] = distancia
        self.distancias[v][u] = distancia

    def calcular_distancia(self, rota):
        distancia_total = 0
        for i in range(len(rota) - 1):
            distancia_total += self.distancias[rota[i]][rota[i + 1]]
        distancia_total += self.distancias[rota[-1]][rota[0]]
        return distancia_total

    def permutacoes(self, inicio, fim):
        if inicio == fim:
            rota = list(range(len(self.vertices)))
            distancia = self.calcular_distancia(rota)
            return rota, distancia

        melhor_rota = None
        melhor_distancia = float('inf')

        for i in range(inicio, fim + 1):
            self.vertices[inicio], self.vertices[i] = self.vertices[i], self.vertices[inicio]
            rota, distancia = self.permutacoes(inicio + 1, fim)

            if distancia < melhor_distancia:
                melhor_distancia = distancia
                melhor_rota = rota

            self.vertices[inicio], self.vertices[i] = self.vertices[i], self.vertices[inicio]

        return melhor_rota, melhor_distancia

    def caixeiro_viajante(self):
        n = len(self.vertices)
        return self.permutacoes(0, n - 1)


# Exemplo de uso:

path = 'Grafo Pesos.xlsx'
df=pd.read_excel(path)
lista = []
for c in df['Cidade']:
    lista.append(c)
for c in df['Cidade B']:
    lista.append(c)

cidades = list(set(lista))
#cidades = ['A', 'B', 'C', 'D']
grafo = Grafo(cidades)
for i, a in df.iterrows():
    i = 0
    t = len(cidades)
    while i < t:
        print("a"+str(i))
        if a.iloc[0] == cidades[i]:
            pA = i
        if a.iloc[1] == cidades[i]:
            pB = i
        i=i+1
    grafo.adicionar_aresta(pA, pB, a.iloc[2])

melhor_rota, melhor_distancia = grafo.caixeiro_viajante()
print(f"Melhor rota: {[cidades[i] for i in melhor_rota]}")
print(f"Distância total: {melhor_distancia}")
