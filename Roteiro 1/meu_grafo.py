# Tratamento de erro para importações
try:
  from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
  import itertools
  import operator
except Exception as e:
  print(e)

# Criação de classe MeuGrafo
class MeuGrafo(GrafoListaAdjacencia):
  def criar_lista_arestas(self): # Criar lista de arestas
    listaArestas = []
    for chave in self.A:
      listaArestas.append([self.A[chave].getV1(), self.A[chave].getV2()])
    return listaArestas

  def vertices_nao_adjacentes(self): # Imprimir vértices não adjacentes
    listaArestas = self.criar_lista_arestas()
    listaVertices = self.N
    haAdjacente = True
    for subset in itertools.combinations(listaVertices, 2):
      if (list(subset) in listaArestas) == False:
        a = list(subset)
        print(a[0], "->", a[1])
        haAdjacente = False
    if haAdjacente:
      print("Não há vértices adjacentes.")

  def ha_laco(self): # Retornar booleano caso haja um laço
    for chave in self.A:
      if self.A[chave].getV1() == self.A[chave].getV2():
        return True
    return False

  def ha_paralelas(self): # Retornar booleano caso haja uma paralela
    listaArestas = self.criar_lista_arestas()
    for i in range(len(listaArestas)):
      if listaArestas[i] in listaArestas[i + 1::]:
        return True
    return False

  def grau(self, V=''): # Retorna o grau do vértice V
    if self.verticeValido(V):  
      cont = 0
      listaArestas = self.criar_lista_arestas()
      for i in listaArestas:
        if i[0] == V:
          cont += 1
        if i[1] == V:
          cont += 1
      return cont
    return 0

  def arestas_sobre_vertice(self, V): # Imprimir as arestas conectadas ao vértice V
    if self.verticeValido(V):
      listaArestas = []
      for chave in self.A:
        listaArestas.append([self.A[chave].getV1(), self.A[chave].getV2(), chave])
      for i in listaArestas:
        if V in i:
          print(i[2])
    return 0

  def eh_completo(self): # Retorna booleano caso grafo seja completo
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
