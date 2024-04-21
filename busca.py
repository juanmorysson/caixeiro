from classes import buscar_vertice, Caminho, Aresta, existe_aresta


def forca_bruta(grafo, inicio):
    # O(1)
    arestas = grafo.arestas
    # O(1)
    c = Caminho()
    # O(1)
    c.adicionar_vertice(inicio)
    # T(1) = 1
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
            c.arestas.pop()
        v = a.proximo_vertice(vertice)
        c.adicionar_aresta(a)
        c.adicionar_vertice(v)
        if v == inicio:
            pass
        else:
            proxima_linha(v, c, arestas, inicio)
    if len(arestas_disponiveis)<1:
        estatisticas(c, inicio, arestas)


def estatisticas(caminho, inicio, arestas):
    if len(caminho.vertices)>14:
        c1 = Caminho()
        for a1 in caminho.arestas:
            c1.adicionar_aresta(a1)
        for v1 in caminho.vertices:
            c1.adicionar_vertice(v1)
        a = existe_aresta(inicio, caminho.ultimo_vertice(), arestas)
        if a is not None:
            print("Caminho:::::::::")
            c1.adicionar_vertice(inicio)
            print("Quantidade de Vértices Visitados: "+str(len(c1.vertices)))
            print(c1.vertices)
            custo = 0.0
            for ar in caminho.arestas:
                custo = custo + float(ar.peso)
            if a is not None:
                custo = custo + float(a.peso)
            print("Custo Total: "+str(round(custo, 2)))

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
