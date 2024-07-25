import networkx as nx
import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('spotify_data.csv', nrows=1000)
print(df.head())

# Crear un grafo vacío
G = nx.Graph()

# Agregar nodos al grafo
for _, row in df.iterrows():
    G.add_node(row['track_id'], artist_name=row['artist_name'], track_name=row['track_name'], popularity=row['popularity'],
               year=row['year'], genre=row['genre'], danceability=row['danceability'], energy=row['energy'],
               key=row['key'], loudness=row['loudness'], mode=row['mode'], speechiness=row['speechiness'],
               acousticness=row['acousticness'], instrumentalness=row['instrumentalness'], liveness=row['liveness'],
               valence=row['valence'], tempo=row['tempo'], duration_ms=row['duration_ms'], time_signature=row['time_signature'])

# (Opcional) Si deseas agregar aristas basadas en alguna similitud o criterio
# Por ejemplo, puedes agregar aristas entre canciones del mismo artista
for artist, group in df.groupby('artist_name'):
    for i in range(len(group)):
        for j in range(i + 1, len(group)):
            G.add_edge(group.iloc[i]['track_id'], group.iloc[j]['track_id'])

# Ahora puedes usar NetworkX para análisis, visualización, etc.
