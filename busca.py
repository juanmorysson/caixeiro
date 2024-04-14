from classes import buscar_vertice


def forca_bruta(grafo, inicio):
    caminho=[]
    arestas = grafo.arestas
    vertices = grafo.vertices
    vertice = inicio
    while len(vertices) > 0:
        print("AAA")
        a, vertices, arestas, vertice = escolher_aresta(vertice, arestas, vertices)
        if a is not None:
            caminho.append(a)
            print("Caminho adicionado" + str(a))
        else:
            print("Backtrack")
            aresta_back = caminho[len(caminho)-1]
            print(aresta_back)
            print(vertice)
            arestas.append(aresta_back)
            vertices.append(vertice)
            if vertice == aresta_back.pontoA:
                back_vertice = aresta_back.pontoB
            else:
                back_vertice = aresta_back.pontoA
            caminho.remove(aresta_back)
            nova_ultima = caminho(len(caminho)-1)
            if back_vertice == nova_ultima.pontoA:
                vertice = nova_ultima.pontoB
            else:
                vertice = nova_ultima.pontoA
            a, vertices, arestas, vertice = escolher_aresta(vertice, arestas, vertices)
            #back tracking
    print("BBB")
    for c in caminho:
        print("CC")
        print(c)

def escolher_aresta(vertice, arestas, vertices):
    print(vertice)
    print(vertices)
    for a in arestas:
        if a.pontoA == vertice:
            if buscar_vertice(vertice.nome, vertices) is not None:
                arestas.remove(a)
                vertices.remove(vertice)
                return a, vertices, arestas, a.pontoB
        if a.pontoB == vertice:
            if buscar_vertice(vertice.nome, vertices) is not None:
                arestas.remove(a)
                vertices.remove(vertice)
                return a, vertices, arestas, a.pontoA
    return None, vertices, arestas, vertice