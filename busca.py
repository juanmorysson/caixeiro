from classes import buscar_vertice, Caminho, Aresta


def forca_bruta(grafo, inicio):
    arestas = grafo.arestas
    c = Caminho("A", True)
    c.adicionar_vertice(inicio)
    proxima_linha(inicio, c, arestas, inicio)

def proxima_linha(vertice, c, arestas, inicio):
    arestas_disponiveis = listar_arestas_p_caminho(vertice, arestas, c.vertices)
    for index, a in enumerate(arestas_disponiveis):
        achou = False
        vertices_a_remover = []
        for vert in c.vertices:
            if achou == True:
                vertices_a_remover.append(vert)
            if vert == vertice:
                achou = True
        for vert in vertices_a_remover:
            c.vertices.remove(vert)
        v = a.proximo_vertice(vertice)
        c.adicionar_aresta(a)
        c.adicionar_vertice(v)
        if v == inicio:
            pass
            #print(v.nome)
        else:
            proxima_linha(v, c, arestas, inicio)
        vertice_anterior = v
        aresta_anterior = a
    estatisticas(c)


def estatisticas(caminho):
    print(caminho)
    print("Quantidade de Vértices Visitados:")
    print(len(caminho.vertices))
    print(caminho.vertices)
    print("Custo Total:")
    custo = 0.0
    for a in caminho.arestas:
        custo = custo + float(a.peso)
    print(custo)

def listar_arestas_p_caminho(vertice, arestas, vertices_do_caminho):
    retorno = []
    for a in arestas:
        if a.pontoA == vertice:
            if buscar_vertice(a.pontoB.nome, vertices_do_caminho) is None:
                retorno.append(a)
        if a.pontoB == vertice:
            if buscar_vertice(a.pontoA.nome, vertices_do_caminho) is None:
                retorno.append(a)
    return retorno
