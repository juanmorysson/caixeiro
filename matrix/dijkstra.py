class Vertice:
    def __init__(self, indice, distancia, pai):
        self.indice = indice
        self.distancia = distancia
        self.pai = pai

    def __lt__(self, other):
        return self.indice < other.indice

def dijkstra(grafo, vertices, inicio):
    Q = []
    for i, v in enumerate(vertices):
        if i == inicio:
            Q.append(Vertice(i, 0, None))
        else:
            Q.append(Vertice(i, float("inf"), None))
    S = []
    while len(Q)>0:
        #extrair menor
        menor = float("inf")
        indice_menor = -1
        for i, v in enumerate(Q):
            if v.distancia < menor:
                indice_menor = i
                menor = v.distancia
        vertice = Q[indice_menor]
        S.append(vertice)
        Q.__delitem__(indice_menor)
        #relax
        adjs = list_adjacentes(grafo, vertice.indice)
        for v in adjs:
            if str(v[0]) != str(inicio):
                for q in Q:
                    if q.indice == v[0]:
                        if q.distancia > vertice.distancia + grafo[vertice.indice][v[0]]:
                            q.distancia = vertice.distancia + grafo[vertice.indice][v[0]]
                            q.pai = vertice.indice

    #retorno
    r = []
    S.sort()
    for s in S:
        r.append(s.distancia)
    return r




def list_adjacentes(grafo,vertice):
    retorno = []
    vertices = grafo[vertice]
    for i, v in enumerate(vertices):
        if v != 0:
            retorno.append([i,v])
    return retorno