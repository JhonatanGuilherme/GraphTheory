try:
  from meu_grafo import MeuGrafo
except Exception as e:
  print(e)

lista = ['J', 'C', 'E', 'P', 'M', 'T', 'Z']
g_p = MeuGrafo(lista)
g_p.adicionaAresta('a1', 'J', 'C')
g_p.adicionaAresta('a2', 'C', 'E')
g_p.adicionaAresta('a3', 'C', 'E')
g_p.adicionaAresta('a4', 'P', 'C')
g_p.adicionaAresta('a5', 'P', 'C')
g_p.adicionaAresta('a6', 'T', 'C')
g_p.adicionaAresta('a7', 'M', 'C')
g_p.adicionaAresta('a8', 'M', 'T')
g_p.adicionaAresta('a9', 'T', 'Z')

#print(g_p.ha_ciclo())
print(g_p.caminho(3))
#print(g_p.conexo())
