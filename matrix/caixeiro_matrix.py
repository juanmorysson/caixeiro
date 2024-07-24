import random

import numpy as np
import pandas as pd
import time

from matrix.dijkstra import dijkstra
from matrix.aleatorio_matrix import aleatorio
from matrix.forca_bruta_matrix import forca_bruta
from matrix.força_bruta_matrix_pos import tsp_brute_force
from matrix.mais_proximo_matrix import mais_proximo

from datetime import datetime

'''
#### cria instância com dados do EXcel
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
cidades.sort()
n = len(cidades)
g = np.zeros((n,n), dtype=np.float64)
#print(cidades)
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
inicio, = np.where(vertices == "Teresina")
'''

data = {'Vertices':  [], 'Arestas': [],
        'tempo_forca_bruta': [], 'tempo_aleatorio': [], 'tempo_vizinho': [],
        'distancia_forca_bruta': [], 'distancia_aleatorio': [],  'distancia_vizinho': [],
        'caminho_forca_bruta': [], 'caminho_aleatorio': [],  'caminho_vizinho': []}
df = pd.DataFrame(data)

#### cria instância com dados aleatórios
tamanhos = [8, 9, 10, 11, 12, 13, 14]#, 15, 16] #[50, 100, 200]
esparso = [0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5 ,6, 0, 0, 0, 0, 0, 0, 0]
medio = [0, 0, 0, 1, 2, 3, 4, 5 ,6, 0, 0, 0]
denso = [0, 1, 2, 3, 4, 5]
tipo = []
tipo.append(esparso)
tipo.append(medio)
tipo.append(denso)
path = 'dataset_result_comb8.xlsx'
for tamanho in tamanhos:
    for k in range(3):
        g2 = np.zeros((tamanho,tamanho), dtype=np.float64)
        for i in range(tamanho):
            c = 0
            for j in range(i,tamanho):
                if j != i:
                    g2[i][j] = random.choice(tipo[k])
                    if g2[i][j] != 0:
                        c += 1
                    if j > tamanho//2:
                        if c < 3:
                            g2[i][j] = random.choice(range(1,6))
                            c += 1
                    g2[j][i] = g2[i][j]
        v2 = []
        for i in range(tamanho):
            v2.append(i)
        count = 0
        for x in g2:
            for e in x:
                if e == 0:
                    count+=1
        l, h = g2.shape
        #percentual_zero = (count-l)/((l*h)-l)
        arestas = (l*h)-count
        mapa = dijkstra(g2, v2, 1)

        print("Iniciando tamanho: "+str(tamanho) +":"+str(arestas)+" - "+str(datetime.now()))
        print("Vizinho mais próximo:" + " - " + str(datetime.now()))
        tempo_mais_proximo = 0.0
        t1 = time.time()
        c = []
        solucao = mais_proximo(g2, 1, caminho=c, retorno=mapa)
        distance_vizinho = solucao[1]
        caminho_vizinho = solucao[0]
        tempo_mais_proximo = time.time() - t1

        print("Aleatório:" + " - " + str(datetime.now()))
        tempo_aleatorio = 0.0
        t1 = time.time()
        c = []
        solucao = aleatorio(g2, 1, caminho=c, retorno=mapa)
        caminho_aleatorio = solucao[0]
        distance_aleatorio = solucao[1]
        tempo_aleatorio = time.time() - t1

        print("Força Bruta Pós:" + " - " + str(datetime.now()))
        #### inicia o algoritmo desejado
        tempo_forca_bruta_pos = 0.0
        t1 = time.time()
        path_pos, distance_forca_bruta = tsp_brute_force(g2, 0, retorno=mapa)
        tempo_forca_bruta_pos = time.time() - t1

        '''
        print("Força Bruta:" +" - "+str(datetime.now()))
        #### inicia o algoritmo desejado
        tempo_forca_bruta = 0.0
        t1 = time.time()
        #retorno = dijkstra(g, vertices, inicio[0])
        #forca_bruta(g, inicio[0], retorno)
        retorno = dijkstra(g2, v2, 1)
        forca_bruta(g2, 1, retorno)
        tempo_forca_bruta = time.time() - t1
        '''
        #genetico(g,inicio[0],5,10, retorno)
        #genetico(g2, 12, 5, 20, retorno2)
        df.loc[len(df) + 1] = [tamanho, arestas,
                               tempo_forca_bruta_pos,  tempo_aleatorio, tempo_mais_proximo,
                               distance_forca_bruta, distance_aleatorio, distance_vizinho,
                               str(path_pos), str(caminho_aleatorio), str(caminho_vizinho)]
        df.to_excel(path, index=False)

