try:
  from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
  from bibgrafo.grafo_exceptions import *
  import copy
except Exception as e:
  print(e)

class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):
  def __init__(self, master):
    super().__init__(master)
    self.dfsGrafo = GrafoMatrizAdjacenciaNaoDirecionado(self.N)
    self.visitedVertices = list(False for i in range(len(self.N)))

  def vertices_nao_adjacentes(self):
    '''
    Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
    Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
    :return: Uma lista com os pares de vértices não adjacentes
    '''
    verticesNaoAdj = list()
    for i in range(len(self.M)):
      for j in range(len(self.M)):
        if i < j and self.M[i][j] == {}:
          verticesNaoAdj.append(f"{self.N[i]}-{self.N[j]}")
    return verticesNaoAdj

  def ha_laco(self):
    '''
    Verifica se existe algum laço no grafo.
    :return: Um valor booleano que indica se existe algum laço.
    '''
    for i in range(len(self.M)):
      if self.M[i][i] != {}:
        return True
    return False

  def grau(self, V=''):
    '''
    Provê o grau do vértice passado como parâmetro
    :param V: O rótulo do vértice a ser analisado
    :return: Um valor inteiro que indica o grau do vértice
    :raises: VerticeInvalidoException se o vértice não existe no grafo
    '''
    if self.existeVertice(V):
      contador = 0
      indice = self.N.index(V)
      for i in self.M[indice]:
        if type(i) == dict and len(i) >= 1:
          contador += len(i)
      for i in range(len(self.M)):
        for j in range(len(self.M)):
          if i <= j and j == indice:
            contador += len(self.M[i][j])
      return contador
    raise VerticeInvalidoException

  def ha_paralelas(self):
    '''
    Verifica se há arestas paralelas no grafo
    :return: Um valor booleano que indica se existem arestas paralelas no grafo.
    '''
    for i in self.M:
      for j in i:
        if len(j) > 1:
          return True
    return False

  def arestas_sobre_vertice(self, V):
    '''
    Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
    :param V: O vértice a ser analisado
    :return: Uma lista os rótulos das arestas que incidem sobre o vértice
    :raises: VerticeInvalidoException se o vértice não existe no grafo
    '''
    if self.existeVertice(V):
      arestasSobreV = list()
      indice = self.N.index(V)
      for i in range(len(self.M)):
        for j in range(len(self.M)):
          if i <= j and (i == indice or j == indice):
            for k in self.M[i][j]:
              if k not in arestasSobreV:
                arestasSobreV.append(k)
      return sorted(arestasSobreV)
    raise VerticeInvalidoException

  def eh_completo(self):
    '''
    Verifica se o grafo é completo.
    :return: Um valor booleano que indica se o grafo é completo
    '''
    if self.ha_laco() or self.ha_paralelas():
      return False
    for i in range(len(self.M)):
      for j in range(len(self.M)):
        if i < j and self.M[i][j] == {}:
          return False
    return True
  
  def eulerPath(self):
    verticesWithOddDegreeVertices = self.__twoOrZeroOddDegreeVertices()
    if not self.__isConnected(self.N[0]) and len(verticesWithOddDegreeVertices) not in [0, 2]:
      return False
    G = copy.deepcopy(self)
    firstVertex = verticesWithOddDegreeVertices[0] if verticesWithOddDegreeVertices else G.N[0]
    return G.__eulerPathReturn(firstVertex)

  def __isConnected(self, V=''):
    index = self.N.index(V)
    self.visitedVertices[index] = True
    if V in self.N:
      for i in range(len(self.M)):
        A = i
        if A > index:
          A, index = index, A
        if self.M[A][index] not in ['-', {}]:
          if not self.visitedVertices[i]:
            self.__isConnected(self.N[i])
      return False if False in self.visitedVertices else True
    raise VerticeInvalidoException
  
  def __twoOrZeroOddDegreeVertices(self):
    counter = 0
    verticesWithOddDegreeVertices = list()
    for vertex in self.N:
      if self.grau(vertex) % 2 != 0:
        counter += 1
        verticesWithOddDegreeVertices.append(vertex)
    return verticesWithOddDegreeVertices if len(verticesWithOddDegreeVertices) in [0, 2] else False
  
  def __eulerPathReturn(self, V='', eulerPath=list()):
    eulerPath.append(V)
    degree, index = self.grau(V), self.N.index(V)
    print(f"ANALISANDO VÉRTICE {V} - GRAU {degree}")
    if degree == 0:
      print("RETORNANDO EULER PATH")
      return eulerPath
    elif degree == 1:
      for i in range(len(self.M)):
        A = i
        if A > index:
          A, index = index, A
        print(f"\nMATRIZ[{A}][{index}] = {self.M[A][index]}")
        if self.M[A][index] not in ['-', {}]:
          print(f"ADICIONANDO {next(iter(self.M[A][index]))} NO PATH E REMOVENDO DO GRAFO...\n")
          eulerPath.append(next(iter(self.M[A][index])))
          self.M[A][index] = dict()
          self.__eulerPathReturn(self.N[i], eulerPath)
    for i in range(len(self.M)):
      A = i
      if A > index:
        A, index = index, A
      print(f"\nMATRIZ[{A}][{index}] = {self.M[A][index]}")
      if self.M[A][index] not in ['-', {}]:
        if self.__isValidEdge(A, index):
          print(f"ADICIONANDO {next(iter(self.M[A][index]))} NO PATH E REMOVENDO DO GRAFO...\n")
          eulerPath.append(next(iter(self.M[A][index])))
          self.M[A][index] = dict()
          self.__eulerPathReturn(self.N[i], eulerPath)
    print(eulerPath)
  
  def __isValidEdge(self, V, U):
    print(f"VALIDANDO ARESTA {self.M[V][U]}\n")
    c1, c2, edgeName = 0, 0, next(iter(self.M[V][U]))
    self.M[V][U] = dict()
    visitedVertices = list(False for i in range(len(self.N)))
    c1 = self.__countConnectedVertices(U, visitedVertices)
    self.adicionaAresta(edgeName, self.N[V], self.N[U])
    c2 = self.__countConnectedVertices(U, visitedVertices)
    if c1 == c2:
      print(f"ARESTA {edgeName} VÁLIDA\n")
      return True
    print(f"ARESTA {edgeName} INVÁLIDA\n")
    return False
  
  def __countConnectedVertices(self, V, visitedVertices):
    count = 1
    visitedVertices[V] = True
    for i in range(len(self.M)):
      A = i
      if A > V:
        A, V = V, A
      if self.M[A][V] not in ['-', {}] and not visitedVertices[i]:
        count += self.__countConnectedVertices(i, visitedVertices)
    return count
  
  def hamiltonianPath(self):
    pass
