class Aresta:
    def __init__(self, pontoA, pontoB, peso):
        self.__pontoA = pontoA
        self.__pontoB = pontoB
        self.__peso = peso

    @property
    def pontoA(self):
        return self.__pontoA

    @property
    def pontoB(self):
        return self.__pontoB

    @property
    def peso(self):
        return self.__peso

    def proximo_vertice(self, v):
        if v == self.__pontoA:
            return self.__pontoB
        else:
            if v == self.__pontoB:
                return self.__pontoA
            else:
                return None
    def __str__(self):
        return f'{self.__pontoA}-{self.__pontoB}: {self.__peso}'

    def __repr__(self):
        return self.__str__()


class Vertice:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def getGrauEntrada(self, listaArestas):
        contadorGrau = 0
        for aresta in listaArestas:
            if aresta.pontoB == self.nome:
                contadorGrau += 1
        return contadorGrau

    def __str__(self):
        return self.__nome

    def __repr__(self):
        return self.__str__()

class Grafo:
    def __init__(self):
        self.__lista_de_Vertices = []
        self.__lista_de_Arestas = []

    @property
    def vertices(self):
        return self.__lista_de_Vertices

    @property
    def arestas(self):
        return self.__lista_de_Arestas

    def adicionar_vertice(self, vertices):
        self.__lista_de_Vertices = vertices

    def adicionar_arestas(self, arestas):
        self.__lista_de_Arestas = arestas

class Caminho:
    def __init__(self):
        self.__lista_de_arestas = []
        self.__lista_de_Vertices = []

    @property
    def vertices(self):
        return self.__lista_de_Vertices

    @property
    def arestas(self):
        return self.__lista_de_arestas
    def adicionar_aresta(self, a):
        self.__lista_de_arestas.append(a)
    def adicionar_vertice(self, v):
        self.__lista_de_Vertices.append(v)
    def remover_aresta(self, a):
        self.__lista_de_arestas.remove(a)
    def remover_vertice(self, v):
        self.__lista_de_Vertices.remove(v)
    def ultimo_vertice(self):
        return self.__lista_de_Vertices[len(self.__lista_de_Vertices)-1]


def buscar_vertice(nome, vertices):
    for v in vertices:
        if v.nome == nome:
            return v
    return None

def existe_aresta(pA, pB, arestas):
    for a in arestas:
        if pA == a.pontoA:
            if pB == a.pontoB:
                return a
        if pA == a.pontoB:
            if pB == a.pontoA:
                return a
    return None
