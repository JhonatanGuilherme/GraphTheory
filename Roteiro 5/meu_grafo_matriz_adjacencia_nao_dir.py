try:
  from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
  from bibgrafo.grafo_exceptions import *
except Exception as e:
  print(e)

class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):
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
