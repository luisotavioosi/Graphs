import networkx as nx
import scipy as sp
import matplotlib.pyplot as plt
G = nx.Graph()


G.add_nodes_from([1,2,3,4,5,6,7])

G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(1,4)
G.add_edge(1,5)
G.add_edge(1,6)

A = nx.adjacency_matrix(G)
print(A.todense())



nx.draw(G, with_labels=True, font_weight='bold')
plt.show()
