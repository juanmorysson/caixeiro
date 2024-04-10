import pandas as pd

from classes import Vertice, Grafo, Aresta

def buscar_vertice(nome, vertices):
    for v in vertices:
        if v.nome == nome:
            return v
    return None

path = 'Grafo Pesos.xlsx'
df=pd.read_excel(path)
lista = []
for c in df['Cidade']:
    lista.append(c)
for c in df['Cidade B']:
    lista.append(c)

cidades = list(set(lista))
print(len(cidades))

vertices = []
for c in cidades:
    vertices.append(Vertice(c))

arestas = []
for i, a in df.iterrows():
    pontoA = buscar_vertice(a.iloc[0], vertices)
    pontoB = buscar_vertice(a.iloc[1], vertices)
    print(a.iloc[2])
    a = Aresta(pontoA, pontoB, a.iloc[2])
    arestas.append(a)

g = Grafo()
g.adicionar_vertice(vertices)
g.adicionar_arestas(arestas)

print("Vértices")
print(g.vertices)
print("")
print("Arestas")
print(g.arestas)

