import csv
import plotly.graph_objects as go
import networkx as nx
from itertools import combinations

def load_collaborations_from_csv(csv_file, max_songs=None):
    G = nx.Graph()
    
    with open(csv_file, mode='r', encoding='utf-8') as archivo_csv:
        archivo = csv.DictReader(archivo_csv)

        song_count = 0

        for row in archivo:
            artists = row['artist_name'].split('&')
            year = row['year']

            # Procesar solo si hay más de un artista en la canción
            if len(artists) > 1:
                if max_songs is not None and song_count >= max_songs:
                    break

                # Eliminar espacios en blanco de los nombres de los artistas
                artists = [artist.strip() for artist in artists]

                # Crear bordes entre todos los pares de artistas en la misma canción
                for artist1, artist2 in combinations(artists, 2):
                    G.add_edge(artist1, artist2)
                
                song_count += 1

    return G

def plot_graph(G):
    pos = nx.spring_layout(G, seed=42)  # Posiciones para los nodos
    edge_trace = go.Scatter(
        x=[],
        y=[],
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines'
    )

    node_trace = go.Scatter(
        x=[],
        y=[],
        text=[],
        mode='markers+text',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            colorscale='YlGnBu',
            size=10,
            colorbar=dict(thickness=15, title='Node Connections', xanchor='left', titleside='right')
        )
    )

    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_trace['x'] += (x0, x1, None)
        edge_trace['y'] += (y0, y1, None)

    for node in G.nodes():
        x, y = pos[node]
        node_trace['x'] += (x,)
        node_trace['y'] += (y,)
        node_trace['text'] += (node,)

    fig = go.Figure(data=[edge_trace, node_trace],
                     layout=go.Layout(
                         showlegend=False,
                         hovermode='closest',
                         margin=dict(b=0, l=0, r=0, t=0),
                         xaxis=dict(showgrid=False, zeroline=False),
                         yaxis=dict(showgrid=False, zeroline=False))
                    )

    fig.show()

def main():
    archivo_csv = 'BaseDatos/spotify_data.csv'
    max_songs = 1000  # Limita el número de canciones a procesar
    G = load_collaborations_from_csv(archivo_csv, max_songs=max_songs)
    plot_graph(G)

if __name__ == '__main__':
    main()