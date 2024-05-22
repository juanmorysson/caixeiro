import numpy as np
import pandas as pd
import time

from matrix.aleatorio_matrix import aleatorio
from matrix.forca_bruta_matrix import forca_bruta
from matrix.mais_proximo_matrix import mais_proximo

# leitura dos dados no Excel
path = '../Grafo Pesos.xlsx'
df=pd.read_excel(path)
#percorre as cidades em cada coluna do Excel
lista = []
for c in df['Cidade']:
    lista.append(c)
for c in df['Cidade B']:
    lista.append(c)
# elimina as cidades duplicadas
cidades = list(set(lista))
n = len(cidades)
g = np.zeros((n,n), dtype=np.float64)
print(cidades)
# alimenta a classe Vertice de objetos
#O(n)
vertices = []
for c in cidades:
    vertices.append(c)
vertices = np.array(vertices)

#alimenta a classe aresta de objetos
#O(n2) pior caso n(n-1)/2
arestas = []
for i, a in df.iterrows():
    i_pontoA, = np.where(vertices == a.iloc[0])
    i_pontoB, = np.where(vertices == a.iloc[1])
    g[i_pontoA[0]][i_pontoB[0]] = a.iloc[2]
    g[i_pontoB[0]][i_pontoA[0]] = a.iloc[2]

tempoExec = 0.0
t1 = time.time()
inicio, = np.where(vertices == "Teresina")
#forca_bruta(g, inicio[0])
#mais_proximo(g, inicio[0])
aleatorio(g, inicio[0])
tempoExec = time.time() - t1
print(round(tempoExec,4))