import pandas as pd
from busca import forca_bruta, listar_arestas_p_caminho
from classes import Vertice, Grafo, Aresta, buscar_vertice

# leitura dos dados no Excel
path = 'Grafo Pesos.xlsx'
df=pd.read_excel(path)
#percorre as cidades em cada coluna do Excel
lista = []
for c in df['Cidade']:
    lista.append(c)
for c in df['Cidade B']:
    lista.append(c)
# elimina as cidades duplicadas
cidades = list(set(lista))

# alimenta a classe Vertice de objetos
vertices = []
for c in cidades:
    vertices.append(Vertice(c))

#alimenta a classe aresta de objetos
arestas = []
for i, a in df.iterrows():
    pontoA = buscar_vertice(a.iloc[0], vertices)
    pontoB = buscar_vertice(a.iloc[1], vertices)
    a = Aresta(pontoA, pontoB, a.iloc[2])
    arestas.append(a)

#cria o grafo
g = Grafo()
#adiciona os vertices
g.adicionar_vertice(vertices)
#adiciona as arestas
g.adicionar_arestas(arestas)

#chama o método de força bruta no arquivo busca.py
forca_bruta(g, buscar_vertice("Teresina", vertices))
