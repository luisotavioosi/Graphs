Teoria dos Grafos
Atividades de Implementação da Disciplina de Teoria dos Grafos

bibliotecas utilizadas na Implementação: Networkx, scipy, matplotlib.pyplot


A inserção de arestas e vértices é feita diretamente no código do arquivo graphs.py


O trecho de código:
G.add_nodes_from([1,2,3,4,5,6,7]) 
cria os nós de 1 a 7.

O trecho de código:
G.add_edge(1,2)
cria uma aresta do nó 1 para o nó 2

O trecho a seguir imprime a matriz de adjacencia para o grafo G.
A = nx.adjacency_matrix(G)
print(A.todense())

O trecho a seguir definir o desenho de G onde diz que será impresso os Labels 1,2,3,4,5,5,6,7 nos respectivos vértices.
e plot exibe o desenho. 
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()
