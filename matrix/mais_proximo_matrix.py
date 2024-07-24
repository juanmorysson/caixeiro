import numpy as np
import sys
sys.setrecursionlimit(300000000)

solucao = []
def mais_proximo(grafo, vertice, caminho = [], invalidos = [], retorno = []):
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
        menor = float('inf')
        v_menor = None
        for vd in vertices_disponiveis:
            if grafo[vertice][vd]<menor:
                menor=grafo[vertice][vd]
                v_menor = vd
        mais_proximo(grafo, v_menor, caminho, invalidos, retorno)
    else:
        m, n = np.array(grafo).shape
        if (len(caminho) < m):
            invalidos.append(caminho.copy())
            caminho.pop()
            vertice = caminho[-1]
            caminho.pop()
            mais_proximo(grafo, vertice, caminho, invalidos, retorno)
        else:
            ultimovertice = caminho[-1]
            custo = 0.0
            aux = -1
            for i in caminho:
                if aux > -1:
                    custo = custo + float(grafo[i][aux])
                aux = i
            custo = custo + retorno[ultimovertice]
            solucao.clear()
            solucao.append(caminho)
            solucao.append(round(custo, 2))
            #print("Caminho: "+str(caminho))
            #print("Custo: "+str(round(custo,2)))
    return solucao

def listar_vertices_adjacentes_disponiveis_p_caminho(vertice, grafo, caminho):
    lista = []
    vertices = grafo[vertice]
    for i, v in enumerate(vertices):
        if v !=0:
            lista.append(i)
    for v in caminho:
        try:
            lista.remove(v)
        except:
            pass
    return lista


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