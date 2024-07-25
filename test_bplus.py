import csv
import random
from song import Song
from b_plus_tree import BPlusTree

def select_attribute():
    attributes = [
        'song_id', 'song_name', 'author', 'genre', 'year',
        'popularity', 'duration'
    ]
    
    print("Selecciona el atributo por el cual quieres ordenar los datos:")
    for i, attr in enumerate(attributes, 1):
        print(f"{i}. {attr}")

    choice = int(input("Ingresa el número correspondiente al atributo: ")) - 1
    if 0 <= choice < len(attributes):
        return attributes[choice]
    else:
        print("Selección no válida. Se usará 'song_name' por defecto.")
        return 'song_name'

def get_data_limit():
    try:
        n = int(input("Ingresa el número de datos a procesar (ejemplo: 10000): "))
        return n
    except ValueError:
        print("Número inválido. Se procesarán 10000 datos por defecto.")
        return 10000

def load_songs_into_bplustree(csv_file, attribute='song_name', n=10000000):
    with open(csv_file, mode='r', encoding='utf-8') as archivo_csv:
        archivo = csv.reader(archivo_csv, delimiter=',')
        next(archivo)  # Omitir el encabezado

        bplustree = BPlusTree()
        songs = []

        for index, fila in enumerate(archivo):
            if index >= n:
                break

            song = Song(
                song_id=fila[3],
                song_name=fila[2],
                author=fila[1],
                genre=fila[6],
                year=fila[5],
                popularity=fila[4],
                duration=fila[18]
            )

            key = getattr(song, attribute)
            bplustree.insert(key, song)  # Ajusta el método de inserción si es necesario
            songs.append(song)

        return bplustree, songs

def demo():
    archivo_csv = 'BaseDatos/spotify_data.csv'
    
    attribute = select_attribute()
    data_limit = get_data_limit()

    bplustree, songs = load_songs_into_bplustree(archivo_csv, attribute=attribute, n=data_limit)

    bplustree.show()

    random_song = random.choice(songs)
    print(f"Querying for song with {attribute} '{getattr(random_song, attribute)}'")
    result = bplustree.search(getattr(random_song, attribute))  # Ajusta el método de búsqueda si es necesario
    if result:
        print(f"Found: {result}")

if __name__ == '__main__':
    demo()
