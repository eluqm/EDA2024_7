# import plotly.graph_objs as go
# import networkx as nx

# G = nx.Graph()
# G.add_edges_from([(1, 2), (2, 3), (3, 4)])

# edge_x = []
# edge_y = []
# for edge in G.edges():
#     x0, y0 = edge[0], edge[1]
#     edge_x.append(x0)
#     edge_y.append(y0)

# fig = go.Figure(data=[go.Scatter(x=edge_x, y=edge_y, mode='markers+lines')])
# fig.show()

import networkx as nx
import plotly.graph_objects as go

# Crear un grafo de ejemplo
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

# Extraer posiciones de los nodos
pos = nx.spring_layout(G)
edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])

# Crear las trazas de aristas y nodos
edge_trace = go.Scatter(x=edge_x, y=edge_y, mode='lines', line=dict(width=0.5, color='#888'))
node_x = [pos[node][0] for node in G.nodes()]
node_y = [pos[node][1] for node in G.nodes()]
node_trace = go.Scatter(x=node_x, y=node_y, mode='markers+text', text=[str(node) for node in G.nodes()],
                        textposition='top center', marker=dict(size=10, color='#1f78b4'))

# Crear la figura
fig = go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(showlegend=False, hovermode='closest', margin=dict(b=0, l=0, r=0, t=0)))

fig.show()
