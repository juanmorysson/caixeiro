import pandas as pd

from busca import forca_bruta
from classes import Vertice, Grafo, Aresta, buscar_vertice

path = 'Grafo Pesos.xlsx'
df=pd.read_excel(path)
lista = []
for c in df['Cidade']:
    lista.append(c)
for c in df['Cidade B']:
    lista.append(c)

cidades = list(set(lista))

vertices = []
for c in cidades:
    vertices.append(Vertice(c))

arestas = []
for i, a in df.iterrows():
    pontoA = buscar_vertice(a.iloc[0], vertices)
    pontoB = buscar_vertice(a.iloc[1], vertices)
    a = Aresta(pontoA, pontoB, a.iloc[2])
    arestas.append(a)

g = Grafo()
g.adicionar_vertice(vertices)
g.adicionar_arestas(arestas)

forca_bruta(g, buscar_vertice("Teresina", vertices))
