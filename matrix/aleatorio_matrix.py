import numpy as np
import sys
import random
sys.setrecursionlimit(300000000)

solucao = []
def aleatorio(grafo, vertice, caminho = [], invalidos = [], retorno = []):
    caminho.append(vertice)
    vertices_disponiveis = listar_vertices_adjacentes_disponiveis_p_caminho(vertice, grafo, caminho)
    #rejeitar caminhos inválidos
    for v in vertices_disponiveis.copy():
        teste = caminho.copy()
        teste.append(v)
        for inv in invalidos:
            if teste == inv:
                vertices_disponiveis.remove(v)
    if len(vertices_disponiveis) > 0:
        aleatorio(grafo, random.choice(vertices_disponiveis), caminho, invalidos, retorno)
    else:
        m, n = np.array(grafo).shape
        if (len(caminho) < m):
            invalidos.append(caminho.copy())
            caminho.pop()
            try:
                vertice = caminho[-1]
            except:
                print(grafo)
                print(vertice)
            caminho.pop()
            aleatorio(grafo, vertice, caminho, invalidos, retorno)
        else:
            ultimovertice = caminho[-1]
            custo = 0.0
            aux = -1
            for i in caminho:
                if aux > -1:
                    custo = custo + float(grafo[i][aux])
                aux = i
            custo = custo + retorno[ultimovertice]
            #print("Caminho: "+str(caminho))
            #print("Custo: "+str(round(custo,2)))
            solucao.clear()
            solucao.append(caminho)
            solucao.append(round(custo,2))
    return solucao

def listar_vertices_adjacentes_disponiveis_p_caminho(vertice, grafo, caminho):
    retorno = []
    vertices = grafo[vertice]
    for i, v in enumerate(vertices):
        if v !=0:
            retorno.append(i)
    for v in caminho:
        try:
            retorno.remove(v)
        except:
            pass
    return retorno


'''
g = np.zeros((5,5), dtype=np.float64)
g[0][1] = 4
g[1][0] = 4
g[0][2] = 2
g[2][0] = 2
g[0][3] = 3
g[3][0] = 3
g[1][2] = 3
g[2][1] = 3
g[1][4] = 4
g[4][1] = 4
g[1][3] = 5
g[3][1] = 5
g[2][4] = 4
g[4][2] = 4
'''
#mais_proximo(g, 0)