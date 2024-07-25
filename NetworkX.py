# import networkx as nx
# import matplotlib.pyplot as plt

# G = nx.Graph()
# G.add_edges_from([(1, 2), (2, 3), (3, 4)])
# nx.draw(G, with_labels=True)
# plt.show()


import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo de ejemplo
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

# Posiciones de los nodos
pos = nx.spring_layout(G)

# Dibujar el grafo
nx.draw(G, pos, with_labels=True, labels={n: str(n) for n in G.nodes()},
        node_color='lightblue', node_size=500, font_size=10, font_color='black')

plt.show()
