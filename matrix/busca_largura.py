def busca_largura(grafo, vertices, inicio):
    cor=[]
    dist=[]
    pai=[]
    for g in vertices:
        cor.append("Branco")
        dist.append(float("inf"))
        pai.append(-1)
    cor[inicio]="Cinza"
    dist[inicio]=0
    pai[inicio]=-1
    fila=[]
    fila.append(inicio)
    while len(fila)>0:
        #desfileirar
        u = fila[0]
        fila.__delitem__(0)
        adjacentes = list_adjacentes(grafo, u)
        for v in adjacentes:
            if cor[v] == "Branco":
                cor[v] = "Cinza"
                dist[v] = dist[u] + grafo[u,v]
                pai[v] = u
                #enfileirar
                fila.append(v)
        cor[u] = "Preto"
    print(dist)
    return dist

def list_adjacentes(grafo,vertice):
    retorno = []
    vertices = grafo[vertice]
    for i, v in enumerate(vertices):
        if v != 0:
            retorno.append(i)
    return retorno