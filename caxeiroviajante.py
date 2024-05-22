import time

import pandas as pd

from aleatorio import aleatorio
from forca_bruta import forca_bruta, listar_arestas_p_caminho
from classes import Vertice, Grafo, Aresta, buscar_vertice
from mais_proximo import mais_proximo
import sys

from pso import pso_init

sys.setrecursionlimit(300000000)

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
#O(n)
vertices = []
for c in cidades:
    vertices.append(Vertice(c))

#alimenta a classe aresta de objetos
#O(n2) pior caso n(n-1)/2
arestas = []
for i, a in df.iterrows():
    pontoA = buscar_vertice(a.iloc[0], vertices)
    pontoB = buscar_vertice(a.iloc[1], vertices)
    a = Aresta(pontoA, pontoB, a.iloc[2])
    arestas.append(a)

#cria o grafo
g = Grafo()
#adiciona os vertices
g.adicionar_vertices(vertices)
#adiciona as arestas
g.adicionar_arestas(arestas)

#chama o método de força bruta no arquivo busca.py
#forca_bruta(g, buscar_vertice("Teresina", vertices))

caminho = Grafo()
tempoExec = 0.0
t1 = time.time()

#mais_proximo(g, buscar_vertice("Teresina", vertices), caminho=caminho)
#aleatorio(g, buscar_vertice("Teresina", vertices), caminho=caminho)
pso_init(g, buscar_vertice("Teresina", vertices))

tempoExec = time.time() - t1
print(round(tempoExec,4))
