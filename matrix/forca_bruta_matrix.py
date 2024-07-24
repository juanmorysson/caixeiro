import numpy as np

caminhos = []
retorno = []

def forca_bruta(grafo, inicio, ret):
    for r in ret:
        retorno.append(r)
    caminho = []
    caminho.append(inicio)
    proxima_linha(inicio, caminho, grafo)
    '''
    for c in caminhos:
        print(c)
    '''

def proxima_linha(vertice, caminho, grafo):
    vertices_disponiveis = listar_vertices_adjacentes_disponiveis_p_caminho(vertice, grafo, caminho)
    #print(vertices_disponiveis)
    #print(caminho)
    for index, v in enumerate(vertices_disponiveis):
        achou = False
        vertices_a_remover = []
        for vert in caminho:
            if achou == True:
                vertices_a_remover.append(vert)
            if vert == vertice:
                achou = True
        for vert in vertices_a_remover:
            caminho.remove(vert)
        caminho.append(v)
        #print("QQQ")
        proxima_linha(v, caminho, grafo)
    if len(vertices_disponiveis)<1:
        estatisticas(caminho, grafo)


def estatisticas(caminho, grafo):
    m, n = np.array(grafo).shape
    if len(caminho)>m-1:
        ultimovertice = caminho[-1]
        custo = 0.0
        aux = -1
        for i in caminho:
            if aux > -1:
                custo = custo + float(grafo[i][aux])
            aux = i
        custo = custo + retorno[ultimovertice]
        caminhos.append([caminho.copy(), round(custo, 2)])

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
