import random

from matrix.aleatorio_matrix import aleatorio

class Individuo:
    def __init__(self, id, melhor_caminho, distancia, fitness):
        self.__id = id
        self.__melhor_caminho = melhor_caminho
        self.__distancia = distancia
        self.__fitness = fitness

    @property
    def melhor_caminho(self):
        return self.__melhor_caminho

    @property
    def distancia(self):
        return self.__distancia

    @property
    def fitness(self):
        return self.__fitness

    def set_melhor_caminho(self, melhor_caminho):
        self.__melhor_caminho = melhor_caminho

    def set_distancia(self, distancia):
        self.__distancia = distancia

    def set_fitness(self, fitness):
        self.__fitness = fitness

    def __str__(self):
        return f'{self.__id} : {self.__melhor_caminho}  {self.__distancia}  {self.__fitness}'

def formiga(grafo, inicio, qtd_individuos, rodadas, retorno):
    individuos = []
    print("$$$$$$$$$$ Início ")
    for i in range(qtd_individuos):
        c = []
        solucao = aleatorio(grafo, inicio, caminho=c, retorno=retorno)
        copia = solucao.copy()
        caminho = copia[0]
        custo = copia[1]
        ind = Individuo(i, caminho, custo,None)
        individuos.append(ind)

    individuos = get_fitness(individuos)

    for i in range(rodadas):
        print("############ Rodada "+str(i))
        fitness_s = []
        for ind in individuos:
            fitness_s.append(ind.fitness)
        for ind in individuos:
            novo_caminho = []
            novo_caminho.append(ind.melhor_caminho[0])
            for i, vertice in enumerate(ind.melhor_caminho):
                if vertice != ind.melhor_caminho[-1]:
                    indice_soteado = random.choices(range(qtd_individuos),fitness_s, k=1)[0]
                    sorteado = individuos[indice_soteado]
                    for i, v in enumerate(sorteado.melhor_caminho):
                        if v == vertice:
                            try:
                                novo_caminho.append(sorteado.melhor_caminho[i+1])
                            except:
                                pass
            if caminho_valido(novo_caminho, len(ind.melhor_caminho)):
                # calcular tamanho
                print("novo_caminho")
                print(novo_caminho)
                ultimo_vertice = novo_caminho[-1]
                nova_distancia = 0.0
                aux = -1
                for i in novo_caminho:
                    if aux > -1:
                        nova_distancia = nova_distancia + float(grafo[i][aux])
                    aux = i
                nova_distancia = nova_distancia+retorno[ultimo_vertice]
                #verifica se é melhor
                if ind.distancia > nova_distancia:
                    ind.set_melhor_caminho(novo_caminho)
                    ind.set_distancia(round(nova_distancia,2))
            else:
                print("Caminho Inválido "+str(novo_caminho))
        individuos = get_fitness(individuos)

def get_fitness(individuos):
    total = 0
    for ind in individuos:
        total = total + ind.distancia
    for ind in individuos:
        #-e -1 por que o menor caminho deve ser o de maior chance no sorteio
        ind.set_fitness(1 - ind.distancia/total)
        print(ind)
    return individuos

def caminho_valido(caminho, tamanho):
    vertices = []
    for i in range(tamanho):
        vertices.append(i)
    for v in caminho:
        try:
            vertices.remove(v)
        except:
            return False
    if len(vertices)>0:
        return False
    return True
