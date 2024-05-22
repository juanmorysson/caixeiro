caminhos = []

def forca_bruta(grafo, inicio):
    caminho = []
    caminho.append(inicio)
    proxima_linha(inicio, caminho, grafo, inicio)
    for c in caminhos:
        print(c)

def proxima_linha(vertice, caminho, grafo, inicio):
    vertices_disponiveis = listar_vertices_adjacentes_disponiveis_p_caminho(vertice, grafo, caminho)
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
        proxima_linha(v, caminho, grafo, inicio)
    if len(vertices_disponiveis)<1:
        estatisticas(caminho, inicio, grafo)


def estatisticas(caminho, inicio, grafo):
    if len(caminho)<=14:
        #print(caminho)
        #print("Inválido")
        pass
    else:
        ultimovertice = caminho[-1]
        if grafo[inicio][ultimovertice] == 0:
            #print("Caminho Inválido Final")
            #print(caminho)
            pass
        else:
            caminho.append(inicio)
            #print("Caminho:::::::::"+str(len(caminho)))
            #print(caminho)
            custo = 0.0
            aux = -1
            for i in caminho:
                if aux > -1:
                    custo = custo + float(grafo[i][aux])
                aux = i
            #print("Custo Total: "+str(round(custo, 2)))
            caminhos.append([caminho.copy(), round(custo, 2)])
            caminho.pop()

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
