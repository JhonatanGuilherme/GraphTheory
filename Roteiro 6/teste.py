try:
  from meu_grafo_matriz_adjacencia_nao_dir import MeuGrafo
except Exception as e:
  print(e)

# Grafo da Paraíba
g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
g_p.adicionaAresta('a1', 'J', 'C')
g_p.adicionaAresta('a2', 'C', 'E')
g_p.adicionaAresta('a3', 'C', 'E')
g_p.adicionaAresta('a4', 'P', 'C')
g_p.adicionaAresta('a5', 'P', 'C')
g_p.adicionaAresta('a6', 'T', 'C')
g_p.adicionaAresta('a7', 'M', 'C')
g_p.adicionaAresta('a8', 'M', 'T')
g_p.adicionaAresta('a9', 'T', 'Z') 

# Grafo da Paraíba sem arestas paralelas
g_p_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
g_p_sem_paralelas.adicionaAresta('a1', 'J', 'C')
g_p_sem_paralelas.adicionaAresta('a2', 'C', 'E')
g_p_sem_paralelas.adicionaAresta('a3', 'P', 'C')
g_p_sem_paralelas.adicionaAresta('a4', 'T', 'C')
g_p_sem_paralelas.adicionaAresta('a5', 'M', 'C')
g_p_sem_paralelas.adicionaAresta('a6', 'M', 'T')
g_p_sem_paralelas.adicionaAresta('a7', 'T', 'Z')

# Grafos completos
g_c = MeuGrafo(['J', 'C', 'E', 'P'])
g_c.adicionaAresta('a1','J','C')
g_c.adicionaAresta('a2', 'J', 'E')
g_c.adicionaAresta('a3', 'J', 'P')
g_c.adicionaAresta('a4', 'E', 'C')
g_c.adicionaAresta('a5', 'P', 'C')
g_c.adicionaAresta('a6', 'P', 'E')

# Grafos com laço
g_l1 = MeuGrafo(['A', 'B', 'C', 'D'])
g_l1.adicionaAresta('a1', 'A', 'A')
g_l1.adicionaAresta('a2', 'A', 'B')
g_l1.adicionaAresta('a3', 'A', 'A')

g_l2 = MeuGrafo(['A', 'B', 'C', 'D'])
g_l2.adicionaAresta('a1', 'A', 'B')
g_l2.adicionaAresta('a2', 'B', 'B')
g_l2.adicionaAresta('a3', 'B', 'A')

g_l3 = MeuGrafo(['A', 'B', 'C', 'D'])
g_l3.adicionaAresta('a1', 'C', 'A')
g_l3.adicionaAresta('a2', 'C', 'C')
g_l3.adicionaAresta('a3', 'D', 'D')
g_l3.adicionaAresta('a4', 'D', 'D')

# Grafos não direcionados
g_nd = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])
g_nd.adicionaAresta('a1', 'A', 'B')
g_nd.adicionaAresta('a2', 'A', 'G')
g_nd.adicionaAresta('a3', 'A', 'J')
g_nd.adicionaAresta('a4', 'G', 'K')
g_nd.adicionaAresta('a5', 'J', 'K')
g_nd.adicionaAresta('a6', 'G', 'J')
g_nd.adicionaAresta('a7', 'I', 'J')
g_nd.adicionaAresta('a8', 'G', 'I')
g_nd.adicionaAresta('a9', 'G', 'H')
g_nd.adicionaAresta('a10', 'F', 'H')
g_nd.adicionaAresta('a11', 'B', 'F')
g_nd.adicionaAresta('a12', 'B', 'G')
g_nd.adicionaAresta('a13', 'B', 'C')
g_nd.adicionaAresta('a14', 'C', 'D')
g_nd.adicionaAresta('a15', 'D', 'E')
g_nd.adicionaAresta('a16', 'B', 'D')
g_nd.adicionaAresta('a17', 'B', 'E')

# Grafos para testes em Caminho Euleriano
k5 = MeuGrafo(['A', 'B', 'C', 'D', 'E'])
k5.adicionaAresta('1', 'A', 'B')
k5.adicionaAresta('2', 'B', 'C')
k5.adicionaAresta('3', 'C', 'D')
k5.adicionaAresta('4', 'D', 'E')
k5.adicionaAresta('5', 'A', 'C')
k5.adicionaAresta('6', 'A', 'D')
k5.adicionaAresta('7', 'A', 'E')
k5.adicionaAresta('8', 'B', 'D')
k5.adicionaAresta('9', 'B', 'E')
k5.adicionaAresta('10', 'C', 'E')

fleuryExample = MeuGrafo(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
fleuryExample.adicionaAresta('a1', 'a', 'b')
fleuryExample.adicionaAresta('a2', 'a', 'c')
fleuryExample.adicionaAresta('a3', 'a', 'd')
fleuryExample.adicionaAresta('a4', 'a', 'f')
fleuryExample.adicionaAresta('a5', 'b', 'c')
fleuryExample.adicionaAresta('a6', 'b', 'e')
fleuryExample.adicionaAresta('a7', 'b', 'g')
fleuryExample.adicionaAresta('a8', 'e', 'f')
fleuryExample.adicionaAresta('a9', 'f', 'g')

print(k5.eulerPath())
#print(fleuryExample.eulerPath())
