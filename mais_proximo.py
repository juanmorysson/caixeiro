from classes import Grafo, buscar_vertice


def mais_proximo(grafo, vertice, aresta = None, caminho = Grafo(), invalidos = []):
    # O(1)
    #print(vertice)
    caminho.adicionar_vertice(vertice)
    if aresta != None:
        caminho.adicionar_aresta(aresta)
    # T(1) = 1
    arestas_disponiveis = []
    for a in grafo.arestas:
        if a.pontoA == vertice:
            if buscar_vertice(a.pontoB.nome, caminho.vertices) is None:
                teste = Grafo()
                for v1 in caminho.vertices:
                    teste.adicionar_vertice(v1)
                teste.adicionar_vertice(a.pontoB)
                if not caminho_invalido(teste, invalidos):
                    arestas_disponiveis.append(a)
        if a.pontoB == vertice:
            if buscar_vertice(a.pontoA.nome, caminho.vertices) is None:
                teste = Grafo()
                for v1 in caminho.vertices:
                    teste.adicionar_vertice(v1)
                teste.adicionar_vertice(a.pontoA)
                if not caminho_invalido(teste, invalidos):
                    arestas_disponiveis.append(a)
    if len(arestas_disponiveis) > 0:
        for a in arestas_disponiveis:
            try:
                if a.peso < menor:
                    menor = a
            except:
                menor = a
        if menor.pontoA == vertice:
            novo_vertice = menor.pontoB
        if menor.pontoB == vertice:
            novo_vertice = menor.pontoA
        mais_proximo(grafo, novo_vertice, aresta=menor, caminho=caminho, invalidos=invalidos)
    else:
        c = "; Caminho: "
        for v in caminho.vertices:
            c = c + str(v) + ", "
        custo = 0
        for a in caminho.arestas:
            custo = custo + a.peso
        v = "Válido; "
        if (len(caminho.vertices)<15):
            v = "Inválido "+str(len(caminho.vertices))+"; "
        else:
            existe_aresta_final = False
            for a in grafo.arestas:
                if a.pontoA == caminho.ultimo_vertice():
                    if a.pontoB == buscar_vertice("Teresina", grafo.vertices):
                        existe_aresta_final = True
                if a.pontoB == caminho.ultimo_vertice():
                    if a.pontoA == buscar_vertice("Teresina", grafo.vertices):
                        existe_aresta_final = True
            if not existe_aresta_final:
                v = "Inválido Final; "
                invalido = Grafo()
                for v1 in caminho.vertices:
                    invalido.adicionar_vertice(v1)
                invalidos.append(invalido)
                vertice = caminho.ultimo_vertice()
                caminho.remover_vertice(vertice)
                aresta = caminho.ultima_aresta()
                caminho.remover_aresta(aresta)
                vertice = caminho.ultimo_vertice()
                caminho.remover_vertice(vertice)
                aresta = caminho.ultima_aresta()
                caminho.remover_aresta(aresta)
                mais_proximo(grafo, caminho.ultimo_vertice(), aresta=caminho.ultima_aresta(), caminho=caminho,
                             invalidos=invalidos)
            else:
                print(v + str(round(custo, 1)) + c)
        #print(v + str(round(custo, 1)) + c)
        if (len(caminho.vertices) < 15):
            invalido = Grafo()
            for v1 in caminho.vertices:
                invalido.adicionar_vertice(v1)
            invalidos.append(invalido)
            caminho.remover_aresta(aresta)
            caminho.remover_vertice(vertice)
            if len(caminho.vertices)>=1:
                vertice = caminho.ultimo_vertice()
                caminho.remover_vertice(vertice)
                aresta = caminho.ultima_aresta()
                if len(caminho.arestas) > 1:
                    caminho.remover_aresta(aresta)
                mais_proximo(grafo, vertice, aresta=caminho.ultima_aresta(), caminho=caminho, invalidos=invalidos)

def caminho_invalido(caminho, invalidos):
    for inv in invalidos:
        if len(inv.vertices)>=len(caminho.vertices):
            invalido = True
            for i in range(0, len(caminho.vertices)):
                if caminho.vertices[i] != inv.vertices[i]:
                    invalido = False
            if invalido == True:
                return True
    return False
