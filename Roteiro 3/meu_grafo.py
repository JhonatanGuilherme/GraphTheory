# Tratamento de erro para importações
try:
  from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
  from bibgrafo.grafo_exceptions import *
  import itertools
  import operator
except Exception as e:
  print(e)

# Criação de classe MeuGrafo
class MeuGrafo(GrafoListaAdjacencia):
  def __init__(self, master):
    super().__init__(master)
    self.C = 0
    self.bfsGrafo = GrafoListaAdjacencia(self.N)
    self.listaVertices = []
  
  def criar_lista_arestas(self): # Criar lista de arestas
    listaArestas = []
    for chave in self.A:
      listaArestas.append([self.A[chave].getV1(), self.A[chave].getV2()])
    return listaArestas

  def vertices_nao_adjacentes(self): # Imprimir vértices não adjacentes
    '''
      Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
      Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
      :return: Uma lista com os pares de vértices não adjacentes
    '''
    listaArestas = self.criar_lista_arestas()
    listaVertices = self.N
    listaVerticesNaoAdjacentes = []
    for subset in itertools.permutations(listaVertices, 2):
      if (list(subset) in listaArestas) == False and (list(subset)[::-1] in listaArestas) == False:
        a = list(subset)
        listaVerticesNaoAdjacentes.append(a[0] + '-' + a[1])
    return listaVerticesNaoAdjacentes

  def ha_laco(self): # Retornar booleano caso haja um laço
    '''
      Verifica se existe algum laço no grafo.
      :return: Um valor booleano que indica se existe algum laço.
    '''
    for chave in self.A:
      if self.A[chave].getV1() == self.A[chave].getV2():
        return True
    return False

  def ha_paralelas(self): # Retornar booleano caso haja uma paralela
    '''
      Verifica se há arestas paralelas no grafo
      :return: Um valor booleano que indica se existem arestas paralelas no grafo.
    '''
    listaArestas = self.criar_lista_arestas()
    for i in range(len(listaArestas)):
      if listaArestas[i] in listaArestas[i + 1::]:
        return True
    return False

  def grau(self, V=''): # Retorna o grau do vértice V
    '''
      Provê o grau do vértice passado como parâmetro
      :param V: O rótulo do vértice a ser analisado
      :return: Um valor inteiro que indica o grau do vértice
      :raises: VerticeInvalidoException se o vértice não existe no grafo
    '''
    if V in self.N:
      cont = 0
      listaArestas = self.criar_lista_arestas()
      for i in listaArestas:
        if i[0] == V:
          cont += 1
        if i[1] == V:
          cont += 1
      return cont
    raise VerticeInvalidoException

  def arestas_sobre_vertice(self, V): # Imprimir as arestas conectadas ao vértice V
    '''
      Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
      :param V: O vértice a ser analisado
      :return: Uma lista os rótulos das arestas que incidem sobre o vértice
      :raises: VerticeInvalidoException se o vértice não existe no grafo
    '''
    if V in self.N:
      listaArestas = []
      listaArestasSobreVertice = []
      for chave in self.A:
        listaArestas.append([self.A[chave].getV1(), self.A[chave].getV2(), chave])
      for i in listaArestas:
        if V in i:
          listaArestasSobreVertice.append(i[2])
      return listaArestasSobreVertice
    raise VerticeInvalidoException

  def eh_completo(self): # Retorna booleano caso grafo seja completo
    '''
      Verifica se o grafo é completo.
      :return: Um valor booleano que indica se o grafo é completo
    '''
    listaArestas = self.criar_lista_arestas()
    listaContagem = [0] * len(self.N)
    listaVertices = self.N
    tamanhoListaVertices = len(listaVertices)
    for i in range(len(listaVertices)):
      for j in listaArestas:
        listaContagem[i] += (j.count(listaVertices[i]))
    if (all(map(operator.eq, listaContagem, [tamanhoListaVertices - 1] * (tamanhoListaVertices - 1))) and 
        self.ha_laco() == False and self.ha_paralelas() == False):
      return True
    return False

  def bfs(self, V=''):
    if V in self.N:
      if len(self.N) == len(self.listaVertices):
        self.C = 0
        self.listaVertices = []
        bfsGrafoRetorno = self.bfsGrafo
        self.bfsGrafo = MeuGrafo(self.N)
        return bfsGrafoRetorno
      tamListaVertices = len(self.listaVertices)
      if tamListaVertices == 0:
        self.listaVertices.append(V)
      for i in self.A:
        if (V != self.A[i].getV1()) and (V == self.A[i].getV2()) and (self.A[i].getV1() not in self.listaVertices):
          self.listaVertices.append(self.A[i].getV1())
          self.bfsGrafo.adicionaAresta(i, self.A[i].getV1(), self.A[i].getV2())
        elif (V != self.A[i].getV2()) and (V == self.A[i].getV1()) and (self.A[i].getV2() not in self.listaVertices):
          self.listaVertices.append(self.A[i].getV2())
          self.bfsGrafo.adicionaAresta(i, self.A[i].getV1(), self.A[i].getV2())
      self.C += 1
      return self.bfs(self.listaVertices[self.C])
    raise VerticeInvalidoException
