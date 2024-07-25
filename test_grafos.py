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
