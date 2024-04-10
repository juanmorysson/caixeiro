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
        return [vertice.__str__() for vertice in self.__lista_de_Vertices]

    @property
    def arestas(self):
        return [aresta.__str__() for aresta in self.__lista_de_Arestas]

    def adicionar_vertice(self, vertices):
        self.__lista_de_Vertices = vertices

    def adicionar_arestas(self, arestas):
        self.__lista_de_Arestas = arestas