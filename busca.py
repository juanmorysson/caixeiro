from classes import buscar_vertice, Caminho, Aresta


def forca_bruta(grafo, inicio):
    arestas = grafo.arestas
    arestas_disponiveis = listar_arestas_p_caminho(inicio, arestas, [])
    for a in arestas_disponiveis:
        c = Caminho("A", True)
        c.adicionar_aresta(a)
        v = a.proximo_vertice(inicio)
        c.adicionar_vertice(v)
        proxima_linha(v, c, arestas)
def proxima_linha(vertice, c, arestas):
    arestas_disponiveis = listar_arestas_p_caminho(vertice, arestas, c.vertices)
    if len(arestas_disponiveis) > 0:
        for index, a in enumerate(arestas_disponiveis):
            v = a.proximo_vertice(vertice)
            c.adicionar_aresta(a)
            c.adicionar_vertice(v)
            proxima_linha(v, c, arestas)
    else:
        estatisticas(c)


def estatisticas(caminho):
    print(caminho)
    print("Quantidade de Vértices Visitados:")
    print(len(caminho.vertices))
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
